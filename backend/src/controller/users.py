import logging

from flask import Blueprint, jsonify, request
from sqlalchemy import or_

from app import db
from model.user import User

users = Blueprint('users', __name__)
Log = logging.getLogger(__name__)


@users.route('/users', methods=['GET'])
def get_users():
    """Endpoint to get a list of active users
    
    Args:
        query (string): user id
        ids (array): a list of id to query
        limit (int): number of items to return

    :return: a list of users
    """
    query = User.query.filter(User.deleted.is_(False))

    if request.args.get("query") is not None:
        condition = request.args.get("query")
        query = query.filter(or_(User.name.like(f"%{condition}%"), User.id.like(f"%{condition}%")))
    
    elif request.args.get("users") is not None:
        query = query.filter(User.id.in_(request.args.getlist("users")))
    
    if request.args.get("limit") is not None:
        query = query.limit(int(request.args.get("limit")))
    
    results = []
    for user in query.all():
        results.append(format_user(user))

    return jsonify({"data": results})


def format_user(user: User):
    return {
        'id': user.id,
        'type': 'user',
        'attributes': {
            'name': user.name,
            'first-name': user.first_name,
            'last-name': user.last_name,
            'title': user.title,
            'email': user.email,
            'deleted': user.deleted
        }
    }