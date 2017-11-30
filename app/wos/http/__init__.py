# -*- coding: utf-8 -*-

from flask import Flask, url_for, redirect, render_template
from flask_login import LoginManager, current_user

from .api import api as api_blueprint
from .frontend import frontend as frontend_blueprint
from ..database import db_session, init_engine
from ..helpers import request_wants_json
from ..services import user_service


def create_app(config):
    '''Create flask application.'''
    app = Flask(__name__)
    app.config.from_pyfile(config)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_filters(app)
    return app


def register_extensions(app):
    app.url_map.strict_slashes = False
    init_engine(app.config.get('DATABASE_URI'))
    login_manager = LoginManager()
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return user_service.get(int(id))


    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('frontend.auth_login'))


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()


    @app.context_processor
    def inject_data():
        if current_user.is_authenticated:
            return dict(
                auth_user=current_user,
            )
        return dict()


def register_blueprints(app):
    app.register_blueprint(frontend_blueprint)
    app.register_blueprint(api_blueprint)


def register_errorhandlers(app):
    def make_error_response(error):
        error_code = 500
        if hasattr(error, 'code'):
            error_code = error.code
        if request_wants_json():
            return jsonify(error={
                'code': error_code,
                'message': str(error),
            }), error.code
        return render_template('errors/%s.html' % error_code, page_title='Uh oh!'), error_code

    for error in (403, 404, 405, 500):
        app.errorhandler(error)(make_error_response)


def register_filters(app):
    @app.template_filter('datetime')
    def filter_datetime(val):
        return format_datetime(val)


    @app.template_filter('date')
    def filter_date(val):
        return format_date(val)
