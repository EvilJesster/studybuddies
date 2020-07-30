from project import mongo, bcrypt
import uuid

users = mongo.db.users
class User: # user class to handle database stuff involving user

    def __init__(self, username, password, unique):
        self.username = username
        self.name = None
        self.studenttype = None
        self.contact = None
        self.strengths = None
        self.weaknesses = None
        self.unique = unique
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def pushdb(self):
        global users
        users.insert({'username': self.username, 'name': self.name, 'password': self.password, 'unique': self.unique, 'pfp': "static/img/questionface.png"})


    @classmethod
    def addmore(cls, unique, data): #TODO fix this jank
        global users
        print(data)
        uinfo = data['userinfo']
        name = uinfo['name']
        studenttype = uinfo['studenttype']
        contact = uinfo['contact']
        math = data['math']
        business = data['business']
        science = data['science']
        engineering = data['engineering']
        humanities = data['humanities']
        art = data['art']
        filt = {'unique': unique}
        builder = {'$set': {'name': name, 'type': studenttype, 'contact':contact,
                            'math': math, 'business': business, 'science': science, 'engineering': engineering,
                            'humanities': humanities, 'art': art}}
        users.update_one(filt, builder )

    @classmethod
    def follow(cls, unique, target):
        foll = mongo.db.followlist



    @classmethod
    def addpfp(cls, url, unique):
        global users
        filt = {'unique': unique}
        users.update_one(filt, {'$set':{'pfp': url}})
    @classmethod
    def authenticate(cls, username, password):
        global users
        login_user = users.find_one({'username' :username})

        if login_user:
            authenticated_user= bcrypt.check_password_hash(login_user['password'], password)
            if authenticated_user:
                return login_user
        return(False)