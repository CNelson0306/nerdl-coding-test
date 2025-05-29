import pymysql
import os


class DB:
    _host = os.environ.get("MYSQL_HOST")
    _port = int(os.environ.get("MYSQL_PORT"))
    _dbname = os.environ.get("MYSQL_DATABASE")
    _username = os.environ.get("MYSQL_USER")
    _password = os.environ.get("MYSQL_PASSWORD")

    _connection = None

    def __init__(self):
        self._connection = pymysql.connect(
            host=self._host,
            user=self._username,
            passwd=self._password,
            db=self._dbname
        )

    def connection(self):
        return self._connection
