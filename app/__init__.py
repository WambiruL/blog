from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
import os

bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager =LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
#initializing app
def create_app(config_name):
    app=Flask(__name__)

# Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

 # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
