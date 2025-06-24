from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proy_bd.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from app.views.user_profile_view import user_profile_view
    app.register_blueprint(user_profile_view)

    from app.views.admin_profile_view import admin_profile_view
    app.register_blueprint(admin_profile_view)

    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app