# -*- coding: utf-8 -*-

from flask import jsonify, request

from . import api


@api.route('/test')
def test():
    return 'Hello World', 200
