from flask import Blueprint, render_template, request, redirect, url_for, flash
from util.enviar_mensaje import send_email as enviar_mensaje
from flask_wtf.csrf import CSRFProtect, CSRFError

blueprint = Blueprint('index_routes', __name__)
csrf = CSRFProtect()

@blueprint.route('/')
@blueprint.route('/inicio.html')
@blueprint.route('/index.html')
@blueprint.route('/inicio')
def index():      
    
    return render_template('pantallas-cliente/index.html')

@blueprint.route('/contacto', methods=['GET', 'POST'])
@csrf.exempt  # Excluir verificación CSRF para esta ruta
def contacto():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        celular = request.form['celular']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        
        """ if not csrf.validate():
            flash('El token CSRF es inválido. Por favor, inténtalo nuevamente.')
            return redirect(url_for('index_routes.contacto')) """
        
        enviar_mensaje(correo, nombres, apellidos, celular, mensaje)
        
        return redirect(url_for('index_routes.contacto'))
        
    return render_template('pantallas-cliente/contacto.html')

@blueprint.route('/galeria')
def galeria():
    
    return render_template('pantallas-cliente/galeria.html')

@blueprint.route('/sobre-mi')
def sobremi():
    
    return render_template('pantallas-cliente/sobremi.html')

