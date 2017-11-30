# -*- coding: utf-8 -*-

import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint, Boolean, DateTime, Time
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    password = Column(String(93), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    active = Column(Boolean, nullable=False, default=False)
    admin = Column(Boolean, nullable=False, default=False)


    def __init__(self, email, password, active=False, admin=False):
        self.email = email
        self.active = active
        self.admin = admin
        self.change_password(password)


    def __repr__(self):
        return '<User id=%r email=%r active=%r admin=%r>' % (
            self.id,
            self.email,
            self.active,
            self.admin,
        )


    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False


    def is_admin(self):
        return self.admin


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def change_password(self, password):
        self.password = generate_password_hash(password)


    def get_id(self):
        return self.id


    def __repr__(self):
        return '<User id=%r>' % self.id

