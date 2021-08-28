from .models import User,db
db.create_all(app=create_app())