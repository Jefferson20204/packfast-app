from flask import render_template, redirect, url_for, flash, request
from app.models.user import User
from app import db

class UserController:
    @staticmethod
    def get_user_profile(user_id):
        user = User.query.get(user_id)
        if user:
            return render_template('user_profile.html', user=user)
        else:
            flash('User not found.')
            return redirect(url_for('auth.login'))

    @staticmethod
    def update_user_profile(user_id):
        user = User.query.get(user_id)
        if user:
            if request.method == 'POST':
                user.username = request.form['username']
                user.email = request.form['email']
                db.session.commit()
                flash('Profile updated successfully.')
                return redirect(url_for('user.get_user_profile', user_id=user.id))
            return render_template('user_profile.html', user=user)
        else:
            flash('User not found.')
            return redirect(url_for('auth.login'))