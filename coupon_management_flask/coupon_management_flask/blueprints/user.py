from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from coupon_management_flask.repository import user
from coupon_management_flask.response.base_response import BaseResponse
from coupon_management_flask.schemas.user import user_schema, users_schema
from coupon_management_flask.utils.http_status_codes import HTTP_200_OK

user_blueprint = Blueprint(name='user_blueprint', import_name=__name__, url_prefix='/v1/user')


@user_blueprint.get('/')
@jwt_required()
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    users = user.find_all(page, per_page)
    result = users_schema.dump(users.items)
    meta = {
        'page': users.page,
        'pages': users.pages,
        'total_count': users.total,
        'prev_page': users.prev_num,
        'next_page': users.next_num,
        'has_next': users.has_next,
        'has_prev': users.has_prev
    }
    response_data = {'users': result, 'meta': meta}
    response = BaseResponse(http_status='OK', http_status_code=HTTP_200_OK, data=response_data)

    return response.to_dict(), response.http_status_code


@user_blueprint.get('/<int:user_id>')
@jwt_required()
def get_by_id(user_id: int):
    entity = user.find_by_id(user_id)
    result = user_schema.dump(entity)
    response_data = {'user': result}
    response = BaseResponse(http_status='OK', http_status_code=HTTP_200_OK, data=response_data)

    return response.to_dict(), response.http_status_code
