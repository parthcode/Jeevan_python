from user_details import user_details


class UserDetails:
    def __init__(self, user, password):
        self.user = user,
        self.password = password

    def __validate_user_data(self):
        if not user_details:
            return False
        return True

    def check_user_data(self):
        if not self.__validate_user_data():
            return False
        for user_id, password in user_details.items():
            if user_id == self.user and password == self.password:
                return True
        return False
