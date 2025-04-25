from flask import Flask
from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed, identity_loaded

from models import User
from auth import setup_auth_routes
from flask_principal import identity_changed, AnonymousIdentity

app = Flask(__name__)
app.secret_key = 'supersecreto'

# Configurar extensiones
login_manager = LoginManager(app)
principals = Principal(app)

# Definir permisos
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Asignar roles a identity
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    user = load_user(identity.id)
    if user:
        for role in user.roles:
            identity.provides.add(RoleNeed(role))

# Rutas públicas/protegidas
@app.route('/')
def index():
    return 'Inicio público'

@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin():
    return 'Área de admin'

@app.route('/user')
@user_permission.require(http_exception=403)
def user_area():
    return 'Área de usuario'

# Configurar rutas de autenticación
setup_auth_routes(app, login_manager)

if __name__ == '__main__':
    app.run(debug=True)