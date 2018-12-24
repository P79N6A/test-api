import pickle
import logging
import logging.handlers
import logging.config
import SocketServer
import struct
import json
from file_logger import logger_dict
# LOGGER = logging.getLogger(__name__)

class LogRecordStreamHandler(SocketServer.StreamRequestHandler):
    """Handler for a streaming logging request.

    This basically logs the record using whatever logging policy is
    configured locally.
    """

    def handle(self):
        """
        Handle multiple requests - each expected to be a 4-byte length,
        followed by the LogRecord in pickle format. Logs the record
        according to whatever policy is configured locally.
        """
        chunk = None
        try:
            while True:
                chunk = self.connection.recv(4)
                if len(chunk) < 4:
                    break
                # big-endian, unsigned long, unpack, add by pangyue
                slen = struct.unpack('>L', chunk)[0]
                chunk = self.connection.recv(slen)
                while len(chunk) < slen:
                    chunk = chunk + self.connection.recv(slen - len(chunk))
                obj = self.unPickle(chunk)
                record = logging.makeLogRecord(obj)
                self.handleLogRecord(record)
        except:
            # LOGGER.exception('failed to handle chunk: %s' % chunk)
            raise

    def unPickle(self, data):
        rt = json.loads(data)
        #when logging with args exc_info=True, then there has field exception with type []
        if "exception" in rt :
            rt['exception'] = "".join(rt['exception'])
        return rt

    def handleLogRecord(self, record):
        logger = logger_dict.get(record.name)
        # N.B. EVERY record gets logged. This is because Logger.handle
        # is normally called AFTER logger-level filtering. If you want
        # to do filtering, do it at the client end to save wasting
        # cycles and network bandwidth!

        # multi threading log write, the control is completed in logging module(handle),
        # the logger is a global var, in multi threading, it process the para writing request.
        logger.handle(record)


class LogRecordSocketReceiver(SocketServer.ThreadingTCPServer):
    """
    Simple TCP socket-based logging receiver suitable for testing.
    """

    allow_reuse_address = 1
    daemon_threads = True

    def __init__(self, host='localhost',
                 port=9967,
                 handler=LogRecordStreamHandler):
        SocketServer.ThreadingTCPServer.__init__(self, (host, port), handler)
        self.timeout = 1
        self.logname = None

    def serve_until_stopped(self):
        import select

        while True:
            rd, wr, ex = select.select([self.socket.fileno()],
                [], [],
                self.timeout)
            if rd:
                self.handle_request()


def main():
    # logging.config.fileConfig('etc/logging-from-tcp-to-file.conf')
    tcpserver = LogRecordSocketReceiver()
    print('About to start TCP server...')
    tcpserver.serve_until_stopped()


if __name__ == '__main__':
    main()
