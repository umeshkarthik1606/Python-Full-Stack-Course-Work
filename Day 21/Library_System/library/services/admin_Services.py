from library.models.admin import Admin

class AuthService:
    def __init__(self):
        self.admin = Admin("admin", "1234")

    def login(self, username, password):
        return username == self.admin.usernmae and password == self.admin.password
