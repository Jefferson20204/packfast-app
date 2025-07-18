from app.models.inventory import Inventory
from app import db

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user

user_profile_view = Blueprint('user_profile_view', __name__)

@user_profile_view.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    # Inicializa el inventario en sesión si no existe
    if 'temp_inventory' not in session:
        session['temp_inventory'] = []

    # Agregar producto temporal
    if request.method == 'POST' and request.form.get('action') == 'add_item':
        name = request.form.get('item_name')
        quantity = request.form.get('item_quantity')
        price = request.form.get('item_price')
        
        if name and quantity and price:
            new_item = Inventory(name=name, quantity=int(quantity), price=float(price))
            db.session.add(new_item)
            db.session.commit()

            flash('Producto agregado correctamente.', 'success')
        else:
            flash('Faltan datos del producto.', 'danger')

        return redirect(url_for('user_profile_view.user_profile'))

    # Eliminar producto temporal
    if request.method == 'POST' and request.form.get('action') == 'delete_item':
        item_id = int(request.form.get('item_id'))
        item = Inventory.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            flash('Producto eliminado correctamente.', 'success')
        else:
            flash('Producto no encontrado.', 'danger')
        return redirect(url_for('user_profile_view.user_profile'))


    # Renderiza el inventario temporal
    inventory = Inventory.query.all()
    return render_template('user_profile.html', user=current_user, inventory=inventory)