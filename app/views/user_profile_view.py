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
        if name and quantity:
            # Genera un id temporal
            temp_id = len(session['temp_inventory']) + 1
            session['temp_inventory'].append({
                'id': temp_id,
                'name': name,
                'quantity': quantity
            })
            session.modified = True
            flash('Producto agregado temporalmente.', 'success')
        return redirect(url_for('user_profile_view.user_profile'))

    # Eliminar producto temporal
    if request.method == 'POST' and request.form.get('action') == 'delete_item':
        item_id = int(request.form.get('item_id'))
        session['temp_inventory'] = [item for item in session['temp_inventory'] if item['id'] != item_id]
        session.modified = True
        flash('Producto eliminado temporalmente.', 'success')
        return redirect(url_for('user_profile_view.user_profile'))

    # Renderiza el inventario temporal
    inventory = session.get('temp_inventory', [])
    return render_template('user_profile.html', user=current_user, inventory=inventory)