from datetime import datetime
from flask import Blueprint, request

from coupon_management_flask.repository import coupon, user
from flask_jwt_extended import jwt_required, current_user

from coupon_management_flask.exceptions.invalid_request import InvalidRequestException
from coupon_management_flask.response.base_response import BaseResponse
from coupon_management_flask.schemas.coupon import coupon_schema, coupons_schema
from coupon_management_flask.schemas.user import user_schema
from coupon_management_flask.utils.http_status_codes import HTTP_200_OK, HTTP_204_NO_CONTENT

coupon_blueprint = Blueprint(name='coupon_blueprint', import_name=__name__, url_prefix='/v1/coupons')


def validate_coupon_use(current_user_obj, coupon_obj):
    coupon_dict = coupon_schema.dump(coupon_obj)
    current_user_dict = user_schema.dump(current_user_obj)

    # validate conditions for using a coupons
    if coupon_dict.get('active') is False:
        raise InvalidRequestException("کوپن غیر فعال است")
    if coupon_obj.expiration_date < datetime.now():
        raise InvalidRequestException("کوپن منقضی شده است")
    if coupon_dict.get('number_left') == 0:
        raise InvalidRequestException("ظرفیت کوپن تمام شده است")
    if coupon_obj.value > current_user_dict.get('credit'):
        raise InvalidRequestException('کاربر اعتبار کافی برای خرید کوپن را ندارد')
    if coupon_obj in current_user.used_coupons:
        raise InvalidRequestException('کاربر قبلا از این کوپن استفاده کرده است')


@coupon_blueprint.get('/')
@jwt_required()
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    coupons = coupon.find_all(page, per_page)
    result = coupons_schema.dump(coupons.items)
    meta = {
        'page': coupons.page,
        'pages': coupons.pages,
        'total_count': coupons.total,
        'prev_page': coupons.prev_num,
        'next_page': coupons.next_num,
        'has_next': coupons.has_next,
        'has_prev': coupons.has_prev
    }
    response_data = {'coupons': result, 'meta': meta}
    response = BaseResponse(http_status='OK', http_status_code=HTTP_200_OK, data=response_data)

    return response.to_dict(), response.http_status_code


@coupon_blueprint.get('/<string:code>')
@jwt_required()
def get_by_id(code: str):
    entity = coupon.find_by_code(code)
    result = coupon_schema.dump(entity)
    response_data = {'coupons': result}
    response = BaseResponse(http_status='OK', http_status_code=HTTP_200_OK, data=response_data)

    return response.to_dict(), response.http_status_code


@coupon_blueprint.post('/use/<string:code>')
@jwt_required()
def use_coupon(code: str):
    coupon_obj = coupon.find_by_code(code)
    validate_coupon_use(current_user, coupon_obj)
    # using the coupons
    user.use_coupon(current_user, coupon_obj)
    response = BaseResponse(http_status='UPDATED', http_status_code=HTTP_204_NO_CONTENT, data={})

    return response.to_dict(), response.http_status_code
