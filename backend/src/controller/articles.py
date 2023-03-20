import logging

from flask import Blueprint, jsonify, request

from model.article import Article
from database import session


articles = Blueprint('articles', __name__)
Logger = logging.getLogger(__name__)


@articles.route('/article/<id>', methods=['GET'])
def get_single_article(id):
    """Endpoint to get a single article"""
    article = Article.query.filter_by(id=id).first()
    print(article)
    # TODO: Use marshmallow to parse article to json object
    return jsonify({'data': 'done'}, 200)


@articles.route('/article/add', methods=['POST'])
def add_single_article():
    """Endpoint to add a single article"""
    json_data = request.get_json()
    title = json_data.get('title')
    content = json_data.get('content') or None
    # TODO: Set author with current login context

    if not title:
        return jsonify({'Error': 'The title of the article cannot be empty'}, 505)

    session.add(Article(title=title, content=content))
    session.commit()

    return jsonify({'OK': True}, 202)
