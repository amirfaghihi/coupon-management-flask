from werkzeug.security import generate_password_hash, check_password_hash

from coupon_management_flask.repository import db
from coupon_management_flask.models.usercoupon import user_coupon


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String)

    used_coupons = db.relationship('Coupon', secondary=user_coupon, backref='Users')

    credit = db.Column(db.Integer)

    def __init__(self, username, password, name, credit):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.credit = credit

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
