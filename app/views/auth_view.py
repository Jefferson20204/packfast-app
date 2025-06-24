from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controllers.auth_controller import AuthController

auth_view = Blueprint('auth_view', __name__)

@auth_view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if AuthController.login(username, password):
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('user_profile_view.profile'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html')

@auth_view.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if AuthController.register(username, password):
            flash('Registro exitoso', 'success')
            return redirect(url_for('auth_view.login'))
        else:
            flash('Error en el registro', 'danger')
    return render_template('register.html')