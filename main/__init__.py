from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

# load the instance config
app.config.from_object('main.config')
app.logger.debug(app.config.get('SQLALCHEMY_DATABASE_URI'))

database = SQLAlchemy(app)

database.init_app(app)

from .hello.controller.helloController import bp

#     Blueprints
app.register_blueprint(bp)
