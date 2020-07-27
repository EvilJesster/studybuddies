from project import mongo, bcrypt


class User: # user class to handle database stuff involving user
    users = mongo.db.users
    def __init__(self, username, password):
        self.username = username
        self.name = None
        self.studenttype = None
        self.contact = None
        self.skills = None
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def pushdb(self):
        global users
        users.insert({'username': self.username, 'name': self.name, 'password': self.password })


    @classmethod
    def addmore(cls, username, name, studenttype, contact, skills): #TODO fix this jank
        global users
        filt = {'username': username}
        builder = {'name': name, 'type': studenttype, 'contact':contact, 'skills':skills}
        users.update_one(filt,builder )

    @classmethod
    def authenticate(cls, username, password):
        global users
        login_user = users.find_one({'username' :username})

        if login_user:
            authenticated_user= bcrypt.check_password_hash(login_user['password'], password)
            if authenticated_user:
                return login_user
        return(False)