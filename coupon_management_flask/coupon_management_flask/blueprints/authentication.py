from flask import Blueprint, request

from coupon_management_flask.exceptions.authentication_exception import AuthenticationException
from coupon_management_flask.exceptions.invalid_request import InvalidRequestException
from werkzeug.security import check_password_hash
from coupon_management_flask.models import User
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, current_user

from coupon_management_flask.schemas.user import user_schema
from coupon_management_flask.utils.http_status_codes import HTTP_200_OK

auth_blueprint = Blueprint(name='auth_blueprint', import_name=__name__, url_prefix='/v1/auth')


@auth_blueprint.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        raise InvalidRequestException("Missing username or password")

    user = User.query.filter_by(username=username).first()

    if not user:
        raise AuthenticationException('کاربر یافت نشد')

    if check_password_hash(user.password, password):
        # generates the JWT Token
        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)

        return {'user': user_schema.dump(user),
                'access_token': access_token,
                'refresh_token': refresh_token}
    raise AuthenticationException('نام کاربری یا پسورد نادرست است')


@auth_blueprint.get('/token/refresh')
@jwt_required(refresh=True)
def refresh_use_token():
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}, HTTP_200_OK
