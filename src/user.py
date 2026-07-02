from auth import AuthService


class UserService:

    def __init__(self):
        self.auth = AuthService()

    def authenticate(self):
        return self.auth.login("admin", "123")
