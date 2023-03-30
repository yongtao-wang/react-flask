import logging
import json

from flask import Blueprint, abort, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from model.article import Article, ArticleSchema
from database import Session


Logger = logging.getLogger(__name__)
articles = Blueprint('articles', __name__)
article_schema = ArticleSchema()
session = Session()


@articles.route('/article/<id>', methods=['GET'])
def get_single_article(id):
    """Endpoint to get a single article"""
    article = Article.query.filter_by(id=id, is_deleted=0).first()
    if not article:
        abort(404)
    return jsonify(article_schema.dump(article)), 200


@articles.route('/article/all', methods=['GET'])
def get_all_articles():
    """Endpoint to get all of the articles"""
    articles = Article.query.filter_by(is_deleted=0).all()
    res = [article_schema.dump(a) for a in articles]
    return jsonify(res), 200


@articles.route('/article/add', methods=['POST'])
def add_single_article():
    """Endpoint to add a single article"""
    json_data = request.get_json()
    title = json_data.get('title')
    content = json_data.get('content') or None
    # TODO: Set author with current login context

    if not title:
        abort(505, 'The title of the article cannot be empty.')

    try:
        session.add(Article(title=title, content=content))
        session.commit()
    except SQLAlchemyError as e:
        Logger.exception('Exception when adding new article.', exc_info=True)
        abort(500, 'SQL Error\n' + str(e))

    return jsonify({'OK': True}, 202)
