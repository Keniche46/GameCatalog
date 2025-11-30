from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
    app.config["SECRET_KEY"] = "segredokeni"

    db.init_app(app)
    migrate.init_app(app, db)

    from core.controllers import views
    views.init_app(app)

    return app