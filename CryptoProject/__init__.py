from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from CryptoProject.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


# noinspection PyUnusedLocal
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from CryptoProject.users.routes import users
    from CryptoProject.transactions.routes import transactions
    from CryptoProject.main.routes import main
    from CryptoProject.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(transactions)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
