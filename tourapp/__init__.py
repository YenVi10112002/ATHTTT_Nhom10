from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_admin import Admin
from flask_login import LoginManager



app = Flask(__name__)
app.secret_key = '689567gh$^^&*#%^&*^&%^*DFGH^&*&*^*'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:%s@localhost/mytour?charset=utf8mb4' % quote('Hoang123@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['CART_KEY'] = 'cart'

db = SQLAlchemy(app=app)

login = LoginManager(app=app)