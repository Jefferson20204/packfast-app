from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.user import User
from app.models.inventory import Inventory

admin_profile_view = Blueprint('admin_profile_view', __name__)

@admin_profile_view.route('/admin_profile')
@login_required
def admin_profile():
    if not current_user.is_admin:
        flash('Acceso denegado', 'danger')
        return redirect(url_for('user_profile_view.user_profile'))
    users = User.query.all()
    inventory_items = Inventory.query.all()
    return render_template('admin_profile.html', users=users, inventory_items=inventory_items)