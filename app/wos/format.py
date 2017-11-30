# -*- coding: utf-8 -*-


def format_datetime(val, fmt='%Y-%m-%d %H:%M'):
    '''Convert a string to a datetime.'''
    return val.strftime(fmt)


def format_date(val, fmt='%Y-%m-%d'):
    '''Convert a string to a date.'''
    return val.strftime(fmt)         
