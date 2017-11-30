# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, Markup, url_for, current_app, request
from flask_login import login_required, current_user

from . import frontend
from .forms import ChangePasswordForm, UserSettingsForm
from wos.database import db_session


sidebar_groups = [
    [{
        'url': 'frontend.account_index',
        'name': 'My Account',
        'icon': 'user',
    }, {
        'url': 'frontend.account_settings',
        'name': 'Settings',
        'icon': 'cog',
    }, {
        'url': 'frontend.account_change_password',
        'name': 'Change Password',
        'icon': 'option-horizontal',
    }, {
        'url': 'frontend.account_subscription',
        'name': 'Subscription',
        'icon': 'credit-card',
    }]
]


@frontend.route('/account', methods=['GET'])
@login_required
def account_index():
    return render_template('account/index.html',
        page_title='My Account',
        sidebar_groups=sidebar_groups,
    )


@frontend.route('/account/settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    form = UserSettingsForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db_session.commit()
        flash('Setting saved!', 'info')
    return render_template('account/settings.html',
        page_title='Settings',
        sidebar_groups=sidebar_groups,
        form=form,
    )


@frontend.route('/account/change_password', methods=['GET', 'POST'])
@login_required
def account_change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.change_password(form.new_password.data)
        db_session.commit()
        flash('Password changed!', 'info')
    return render_template('account/change_password.html',
        form=form,
        page_title='Change Password',
        sidebar_groups=sidebar_groups,
    )


@frontend.route('/account/subscription', methods=['GET', 'POST'])
@login_required
def account_subscription():
    return render_template('account/subscription.html',
        page_title='Subscription',
        sidebar_groups=sidebar_groups,
    )
