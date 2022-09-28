from coupon_management_flask.repository import db

user_coupon = db.Table('user_coupon',
                       db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
                       db.Column('coupon_id', db.Integer, db.ForeignKey('Coupon.id'), primary_key=True))
