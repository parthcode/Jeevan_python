from user_details import SignUp

user_id = '1234'
password = 'pdw@123'
name = 'karan'

obj = SignUp(name, user_id, password)
x = {"somenew": {"da": 232}}
obj.create_user_details()
