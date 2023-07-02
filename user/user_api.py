from flask import Blueprint
from database.userservice import get_all_users_db, get_exact_user_db, delete_user_db, register_user_db, check_user_db

user_bp = Blueprint('user', __name__, url_prefix='/user')


# Get all users
@user_bp.route('/', methods=['GET'])
def get_all_users():
    all_users = get_all_users_db()
    return {'status': 1, 'message': all_users}


# Get exact user from user_id
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user(user_id: int):
    get_user = get_exact_user_db(user_id)
    if get_user:
        return {'status': 1, 'message': get_user}

    return {'status': 0, 'message': 'Not Found'}


# Change user data from user id
@user_bp.route('/<int:user_id>', methods=['PUT'])
def change_user_info(user_id: int):
    return {'message': 'hello'}


# Delete user's page
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_exact_user(user_id: int):
    delete_user = delete_user_db(user_id)
    if delete_user:
        return {'status': 1, 'message': 'User deleted'}
    return {'status': 0, 'message': 'Not Found'}

