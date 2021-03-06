"""
Mobile Programing Team Project
수강신청 App Server Side
코드 작성자 20153159 김연수
"""
from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import *

from api.authorization import app as api_authorization
from api.lecture import app as api_lecture
from api.server import app as api_server
from api.test import app as api_test
from settings.logger import after_request, error_handler
from settings.settings import DEBUG, DB_URI


def create_wsgi():
    # app settings
    app = Flask(__name__)
    app.debug = DEBUG  # debug mode
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI  # db connect
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.after_request(after_request)
    app.register_error_handler(InternalServerError, error_handler)

    # app connections
    app.register_blueprint(api_server)
    app.register_blueprint(api_test)
    app.register_blueprint(api_authorization)
    app.register_blueprint(api_lecture)

    CORS(app)
    return app
