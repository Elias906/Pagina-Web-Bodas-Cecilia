from flask import Flask
from flask_wtf.csrf import CSRFProtect

#Manejo de rutas
from routes.index_routes import blueprint as index_blueprint

app = Flask(__name__)
csrf = CSRFProtect(app)

#Llave secreta. Debe ser una diferente que esta.
app.config['SECRET_KEY'] = b'\xd8\xa4j,mp\xa3\xdd\xcb\xd0M\xfc\x96\x1co\x08/\x923\xcb\x8a=\x06\xbb'

#Determinar en qué carpeta se guardarán las imágenes subidas
app.config['UPLOAD_FOLDER'] = 'src/static/uploads'

#Agregar rutas
app.register_blueprint(index_blueprint)

if __name__ == '__main__':
    app.run(debug=True)