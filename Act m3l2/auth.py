from flask import redirect, url_for
from flask_login import login_user, logout_user
from flask_principal import Identity, identity_changed, AnonymousIdentity
from models import users, User

def setup_auth_routes(app, login_manager):
    @app.route('/login/<username>')
    def login(username):
        user_data = users.get(username)
        if user_data:
            user = User(username, user_data['roles'])
            login_user(user)
            identity_changed.send(app, identity=Identity(user.id))
            return f'Logueado como {username}'
        return 'Usuario no encontrado', 404

    @app.route('/logout')
    def logout():
        logout_user()
        identity_changed.send(app, identity=AnonymousIdentity())
        return 'Sesión cerrada'
