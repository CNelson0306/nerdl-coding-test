import falcon
import json
import pymysql

from Helpers.db import DB
from Helpers.db_error_handler import ErrorHandling

class NewsArticles:
    def on_get(self, req, resp, news_article_id=None):
        _cursor, _connection, _news_articles = None, None, []

        try:
            _connection = DB().connection()
            _cursor = _connection.cursor()
        except pymysql.Error as db_error:
            ErrorHandling.database_errors(db_error)

        _query = 'SELECT * FROM news_articles'
        _values = []

        if news_article_id:
            _query += ' WHERE id=%s'
            _values.append(news_article_id)

        try:
            _cursor.execute(_query, _values)
            for row in _cursor:
                _news_article = {
                    'id': row[0],
                    'title': row[1],
                    'excerpt': row[2],
                    'author': row[3],
                    'category': row[4],
                    'image': row[5],
                    'published_date': row[6]
                }

                _news_articles.append(_news_article)
        except pymysql.Error as err:
            ErrorHandling.processing_errors(err)

        _response = {
            "Articles": _news_articles
        }
        resp.body = json.dumps(_response)
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        _cursor, _connection, _new_id = None, None, None

        if not req.media.get("title") or not req.media.get("excerpt") or not req.media.get("author") \
            or not req.media.get("category"):
            raise falcon.HTTPBadRequest('Bad Request')

        try:
            _connection = DB().connection()
            _cursor = _connection.cursor()
        except pymysql.Error as db_error:
            ErrorHandling.database_errors(db_error)

        _query = ('INSERT INTO news_articles (title, excerpt, author, category, image_base64, puyblished_date) '
                  'VALUES (%s, %s, %s, %s, %s, %s, %s)')
        _values = [req.media.get("title"), req.media.get("excerpt"), req.media.get("author"),
                   req.media.get("category"), req.media.get("image_base64"), req.media.get("published_date")]
        
        try:
            _cursor.execute(_query, _values)
            _new_id = _cursor.lastrowid
            _connection.commit()
        except pymysql.Error as err:
            ErrorHandling.processing_errors(err)

        _response = {
            "news_articles_id": _new_id
        }
        resp.body = json.dumps(_response)
        resp.status = falcon.HTTP_OK
