from flask import Blueprint, jsonify
from db import mongodb
from auth import requires_auth

# Blue print construction
users_bp = Blueprint('users_bp', __name__)

# Routes
@users_bp.route('/')
@requires_auth
def get_all_users():
    user_list = []
    for user in mongodb['db'].db.users.find(None, {'_id': False}):
        user_list.append(user)
    return jsonify(user_list)