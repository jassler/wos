# -*- coding: utf-8 -*-

from .core import Service
from .models import User


class UserService(Service):
    __model__ = User


user_service = UserService()
