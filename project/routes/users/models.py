from project import mongo, bcrypt


class User: # user class to handle database stuff involving user
    def __init__(self, username, password):
        self.username = username
        self.name = None
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def pushdb(self):
        users = mongo.db.users
        users.insert({'username': self.username, 'name': self.name, 'password': self.password })

    @classmethod
    def authenticate(cls, username, password):
        users = mongo.db.users
        login_user = users.find_one({'username' :username})

        if login_user:
            authenticated_user= bcrypt.check_password_hash(login_user['password'], password)
            if authenticated_user:
                return login_user
        return(False)