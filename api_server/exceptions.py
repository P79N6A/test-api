# encoding=utf-8

class BaseException(Exception):
    def __init__(self, message, code):
        Exception.__init__(self, '%s: %s' % (message, code))
        self.code = code


class GeneralAPIException(BaseException):
    def __init__(self, message, code):
        Exception.__init__(self, '%s: %s' % (message, code))
        self.code = code
