from datetime import datetime
from coupon_management_flask.repository import db


class Coupon(db.Model):
    __tablename__ = 'Coupon'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    value = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True)
    hidden_code = db.Column(db.String(25))
    number_left = db.Column(db.Integer)
    expiration_date = db.Column(db.DateTime, default=datetime.now())
