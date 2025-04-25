from flask_login import UserMixin

# Simular base de datos de usuarios
users = {
    'admin': {'password': 'admin', 'roles': ['admin']},
    'user': {'password': 'user', 'roles': ['user']}
}

class User(UserMixin):
    def __init__(self, username, roles):
        self.id = username
        self.roles = roles

    @staticmethod
    def get(user_id):
        data = users.get(user_id)
        if data:
            return User(user_id, data['roles'])
        return None
