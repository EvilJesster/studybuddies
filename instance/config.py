from datetime import timedelta
import uuid
SECRET_KEY = uuid.uuid4().hex
MONGO_DBNAME = 'sbud'
MONGO_URI = 'mongodb+srv://admin:cNpYtYImWVUZJvbu@cluster0.j6koj.mongodb.net/sbud?retryWrites=true&w=majority'
#PERMANENT_SESSION_LIFETIME = timedelta(weeks=1)