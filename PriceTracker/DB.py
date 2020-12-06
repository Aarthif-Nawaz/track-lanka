from PriceTracker import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), unique=True, nullable=False)
    email = db.Column(db.String(225), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    tracking = db.relationship('Tracking', backref='Owner', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Tracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.Text, nullable=False)
    product_url = db.Column(db.Text, nullable=False)
    product_name = db.Column(db.Text, nullable=False)
    set_price = db.Column(db.FLOAT, nullable=False)
    current_price = db.Column(db.FLOAT, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.store_name}', '{self.product_url}', '{self.product_name}', '{self.set_price}', '{self.current_price}')"





