from coupon_management_flask.schemas import ma


class CouponSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "value", "hidden_code", "number_left", "expiration_date", "active")


coupon_schema = CouponSchema()
coupons_schema = CouponSchema(many=True)
