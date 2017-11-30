# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
import re
from wtforms import TextField, PasswordField, validators, SelectField, HiddenField
from flask_login import login_user, current_user

from wos.models import User


class LoginForm(FlaskForm):
    email = TextField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])


    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        user = User.query.filter(
            User.email == self.email.data,
        ).first()
        if not user or not user.check_password(self.password.data):
            self.email.errors.append('Email and/or password is incorrect')
            self.password.errors.append(None)
            return False
        if not user.active:
            self.email.errors.append('Account is not activated')
            return False
        login_user(user)
        return True


class RegisterForm(FlaskForm):
    email = TextField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
    confirm_password = PasswordField('Confirm Password', [validators.Required(), validators.EqualTo('password', message='Passwords must match')])


    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        user = User.query.filter(
            User.email == self.email.data,
        ).first()
        if user:
            self.email.errors.append('Email already exists in the system')
            return False
        return True


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current Password', [validators.Required()])
    new_password = PasswordField('New Password', [validators.Required()])
    confirm_new_password = PasswordField('Confirm Password', [validators.Required(), validators.EqualTo('new_password', message='Passwords must match')])


    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not current_user.check_password(self.old_password.data):
            self.old_password.errors.append('Old password is incorrect')
            return False
        return True


class UserSettingsForm(FlaskForm):
    pass
