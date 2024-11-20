from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'

    db.init_app(app)

    # import blueprints here
    from profileapp.blueprints.core.routes import core

    app.register_blueprint(core, url_prefix='/')

    migrate = Migrate(app, db)

    return app
