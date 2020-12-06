from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import PriceTracker.config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_apscheduler import APScheduler
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

conn = "mysql+pymysql://u3avk7ovn1tzaiim:yVLe1C9CiP0J0L6E9Blb@bfgmkqigfxkofpvmcywv-mysql.services.clever-cloud.com:3306/bfgmkqigfxkofpvmcywv"
app = Flask(__name__)
app.config['SECRET_KEY'] = "1291073129749013740932ABFG"
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)
sheduler = APScheduler()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
admin = Admin(app)

from PriceTracker.DB import User,Tracking

admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Tracking,db.session))

from PriceTracker import routes
