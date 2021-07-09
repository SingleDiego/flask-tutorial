from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(Config)
    
    # 初始化各种扩展库
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # 引入蓝图并注册
    from app.main.routes import main_routes
    app.register_blueprint(main_routes)

    from app.auth.routes import auth_routes
    app.register_blueprint(auth_routes)

    from app.errors.routes import errors_routes
    app.register_blueprint(errors_routes)

    return app

from app import models