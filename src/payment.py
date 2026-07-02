from user import UserService


class PaymentService:

    def __init__(self):
        self.user = UserService()

    def process(self):
        return self.user.authenticate()
