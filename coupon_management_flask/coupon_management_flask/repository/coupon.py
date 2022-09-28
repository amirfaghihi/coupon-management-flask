from coupon_management_flask.exceptions.entity_not_found import EntityNotFoundException
from coupon_management_flask.models import Coupon


def find_all(page: int, per_page: int):
    return Coupon.query.filter_by(active=True).order_by(Coupon.id.asc()).paginate(page=page, per_page=per_page)


def find_by_code(code: str):
    entity = Coupon.query.filter_by(hidden_code=code).first()
    if not entity:
        raise EntityNotFoundException
    return entity
