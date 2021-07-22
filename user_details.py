class UserDetails:
    def __init__(self, name, user_id, password):
        self.name = name
        self.user_id = user_id
        self.password = password
        self._validate_password()

    def _get_file_meta_data(self, file_location, mode='r', operation='close'):
        meta_data = open(file_location, mode)
        if operation == 'open':
            return meta_data
        return meta_data.close()

    @classmethod
    def get_user_details(cls, operation=None):
        user_id = input("Enter the user_id")
        password = input("Enter the password")
        if operation == 'sign_up':
            name = input("Enter the name")
            return name, user_id, password # return it as a dict
        return user_id, password

    def _validate_password(self):
        pass


print(UserDetails.get_user_details(operation='sign_up'))
