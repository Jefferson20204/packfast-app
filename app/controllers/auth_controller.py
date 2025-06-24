from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            if user.is_admin:
                return redirect(url_for('admin_profile_view.admin_profile'))
            else:
                return redirect(url_for('user_profile_view.user_profile'))
        else:
            flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('El usuario o correo ya existe', 'danger')
        else:
            User.create_user(username, email, password)
            flash('Registro exitoso', 'success')
            return redirect(url_for('auth.login'))
    return render_template('register.html')