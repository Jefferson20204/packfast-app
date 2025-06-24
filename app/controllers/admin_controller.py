from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.user import User
from app.models.inventory import Inventory

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_dashboard():
    return render_template('admin_profile.html')

@admin_bp.route('/admin/manage_users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        action = request.form.get('action')
        user_id = request.form.get('user_id')
        if action == 'delete':
            User.delete_user(user_id)
            flash('User deleted successfully', 'success')
        elif action == 'promote':
            User.promote_user(user_id)
            flash('User promoted to admin', 'success')
    users = User.get_all_users()
    return render_template('manage_users.html', users=users)

@admin_bp.route('/admin/manage_inventory', methods=['GET', 'POST'])
def manage_inventory():
    if request.method == 'POST':
        action = request.form.get('action')
        item_id = request.form.get('item_id')
        if action == 'add':
            item_name = request.form.get('item_name')
            Inventory.add_item(item_name)
            flash('Item added successfully', 'success')
        elif action == 'delete':
            Inventory.delete_item(item_id)
            flash('Item deleted successfully', 'success')
    inventory_items = Inventory.get_all_items()
    return render_template('manage_inventory.html', inventory_items=inventory_items)