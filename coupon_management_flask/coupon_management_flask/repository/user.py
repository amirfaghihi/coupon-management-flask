from coupon_management_flask.exceptions.database_exception import DatabaseException
from coupon_management_flask.exceptions.entity_not_found import EntityNotFoundException
from coupon_management_flask.models import User
from coupon_management_flask.repository import db


def find_all(page: int, per_page: int):
    return User.query.order_by(User.id.asc()).paginate(page=page, per_page=per_page)


def find_by_id(user_id: int):
    entity = User.query.filter_by(id=user_id).first()
    if not entity:
        raise EntityNotFoundException
    return entity


def use_coupon(user, coupon):
    try:
        user.used_coupons.append(coupon)
        user.credit -= coupon.value
        coupon.number_left -= 1
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise DatabaseException('خطایی در استفاده از کوپن رخ داده است')
