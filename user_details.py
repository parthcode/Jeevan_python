import os
import json


class UserDetails:
    def __init__(self, name, user_id, password):
        self.name = name
        self.user_id = user_id
        self.password = password
        self._validate_password()

    @classmethod
    def get_user_details(cls, operation=None):
        user_id = input("Enter the user_id")
        password = input("Enter the password")
        user_details = {'user_id': user_id,
                        'password': password}
        if operation == 'sign_up':
            name = input("Enter the name")
            user_details.update({'name': name})
            return user_details
        return user_details

    def _validate_password(self):
        pass


class SignUp(UserDetails):
    LOCATION = os.getcwd() + '/user_details.json'

    def __init__(self, name, user_id, password):
        super().__init__(name, user_id, password)

    def create_user_details(self):
        data = json.dumps(self.get_user_data(operation='sign_up'))
        meta_data = open(SignUp.LOCATION, 'r+')
        meta_data.write(data)
        meta_data.close()

    def get_user_data(self, operation):
        if operation == 'sign_up':
            return {"user_id": self.user_id, "name": self.name, "password": self.password}
        return {"name": self.name, "password": self.password}

