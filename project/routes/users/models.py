from project import mongo, bcrypt
import uuid

users = mongo.db.users
class User: # user class to handle database stuff involving user

    def __init__(self, username, password, unique):
        self.username = username
        self.name = None
        self.studenttype = None
        self.contact = None
        self.skills = None
        self.unique = unique
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def pushdb(self):
        global users
        users.insert({'username': self.username, 'name': self.name, 'password': self.password, 'unique': self.unique})


    @classmethod
    def addmore(cls, unique, data): #TODO fix this jank
        global users

        name = data['name']
        studenttype = data['studenttype']
        contact = data['contact']
        skills = data['skills']
        filt = {'unique': unique}
        builder = {'$set': {'name': name, 'type': studenttype, 'contact':contact, 'skills':skills}}
        users.update_one(filt, builder )

    @classmethod
    def authenticate(cls, username, password):
        global users
        login_user = users.find_one({'username' :username})

        if login_user:
            authenticated_user= bcrypt.check_password_hash(login_user['password'], password)
            if authenticated_user:
                return login_user
        return(False)