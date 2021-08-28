from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth.main import auth


app = Flask(__name__)

app.register_blueprint(auth,url_prefix='/auth')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'secret-key-goes-here'

db = SQLAlchemy(app)




# SQLAlchemy database connecting.






if __name__ == '__main__':
    
    from view import *
    app.run(debug=True)