import logging 

from flask import Blueprint, jsonify, request

from model.article import Article

articles = Blueprint('articles', __name__)
Logger = logging.getLogger(__name__)

@articles.route('/article/<id>', methods=['GET'])
def get_article():
  """Endpoint to get a single article by id
  
  """
  # query = Article.query.filter(Article.id.is_())
  pass


@articles.route('/articles/all', methods=['GET'])
def get_articles():
  """Endpoint to get a list of articles
  
  Args:

  :return: a list of articles
  """
  # query = Article.query.filter()
  pass