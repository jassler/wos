# -*- coding: utf-8 -*-

from flask import render_template
from flask_login import login_required

from . import frontend


@frontend.route('/', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard/index.html',
        page_title='Overview',
    )
