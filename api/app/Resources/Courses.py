import falcon
import json
import pymysql

from Helpers.db import DB
from Helpers.db_error_handler import ErrorHandling

class Courses:
    def on_get(self, req, resp, course_id=None):
        _cursor, _connection, _courses = None, None, []

        try:
            _connection = DB().connection()
            _cursor = _connection.cursor()
        except pymysql.Error as db_error:
            ErrorHandling.database_errors(db_error)
        
        _query = 'SELECT * FROM courses'
        _values = []

        if course_id:
            _query += ' WHERE id=%s'
            _values.append(course_id)

        try:
            _cursor.execute(_query, _values)
            for row in _cursor:
                _course = {
                    'id': row[0],
                    'title': row[1],
                    'description': row[2],
                    'duration': row[3],
                    'level': row[4],
                    'section': row[5],
                    'image': row[6],
                    'url': row[7],
                }
                _courses.append(_course)
        except pymysql.Error as err:
            ErrorHandling.processing_errors(err)

        _response = {
            "courses": _courses
        }
        resp.body = json.dumps(_response)
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        _cursor, _connection, _new_id = None, None, None

        if not req.media.get("title") or not req.media.get("description") or not req.media.get("duration") \
            or not req.media.get("level") or not req.media.get("section") or not req.media.get("url"):
            raise falcon.HTTPBadRequest('Bad Request')

        try:
            _connection = DB().connection()
            _cursor = _connection.cursor()
        except pymysql.Error as db_error:
            ErrorHandling.database_errors(db_error)

        _query = ('INSERT INTO courses (title, description, duration, level, section, image_base64, url) '
                  'VALUES (%s, %s, %s, %s, %s, %s, %s)')
        _values = [req.media.get("title"), req.media.get("description"), req.media.get("duration"),
                   req.media.get("level"), req.media.get("section"), req.media.get("image_base64"), req.media.get("url")]


        try:
            _cursor.execute(_query, _values)
            _new_id = _cursor.lastrowid
            _connection.commit()
        except pymysql.Error as err:
            ErrorHandling.processing_errors(err)

        _response = {
            "course_id": _new_id
        }
        resp.body = json.dumps(_response)
        resp.status = falcon.HTTP_OK
