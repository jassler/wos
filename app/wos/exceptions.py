# -*- coding: utf-8 -*-


class WosError(Exception):
    pass


class WosHttpError(WosError):
    '''Base HTTP exception.'''
    def __init__(self, status_code=500, message=None):
        super(ValidationError, self).__init__(message)
        self.status_code = status_code
