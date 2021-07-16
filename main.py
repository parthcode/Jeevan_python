from check_user import UserDetails

user_id = '1234'
password = 'pdw@123'
obj = UserDetails(user_id, password)
print(obj.check_user_data())
