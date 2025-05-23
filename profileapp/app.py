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
    from profileapp.blueprints.profiles.routes import profiles

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(profiles, url_prefix='/profiles')

    migrate = Migrate(app, db)

    return app
