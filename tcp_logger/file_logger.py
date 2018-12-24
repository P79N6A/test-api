import logging
from logstash_formatter import LogstashFormatterV1
from logging.handlers import RotatingFileHandler

json_formatter = LogstashFormatterV1()

#api access file log config
api_logger = logging.getLogger("api_log")
api_logger.setLevel("INFO")
api_hander = RotatingFileHandler("var/log/api.log",'a',1024*1024*20,10)
api_hander.setFormatter(json_formatter)
api_logger.addHandler(api_hander)

#sys logger file config
sys_logger = logging.getLogger("sys_log")
sys_logger.setLevel("INFO")
sys_hander = RotatingFileHandler("var/log/sys.log",'a',1024*1024*20,10)
sys_hander.setFormatter(json_formatter)
sys_logger.addHandler(sys_hander)

#private data logger file config
# private_data_logger = logging.getLogger("private_data_log")
# private_data_logger.setLevel("INFO")
# private_data_hander = RotatingFileHandler("var/log/private_data_log.log",'a',1024*1024*200,10)
# private_data_hander.setFormatter(json_formatter)
# private_data_logger.addHandler(private_data_hander)

logger_dict= {"api_log":api_logger,"sys_log":sys_logger}
