# coding=utf-8


"""
    thread pool 实现
"""

import threading


class ThreadException(Exception):

    def __init__(self, msg=None):
        super(ThreadException, self).__init__()
        self.msg = msg

    def __str__(self):
        return msg if msg is not None and isinstance(msg, basestring) else ""

class ThreadTypeError(ThreadException):
    pass


class ThreadCommand(dict):

    def __init__(self, command=None, run_func=None,  *argv, **kw):
        if run_func is None or not callable(run_func):
            raise ThreadTypeError("")
