from coupon_management_flask.schemas import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "name", "credit")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
