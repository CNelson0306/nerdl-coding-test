import pymysql
import falcon
from pymysql.constants import ER

CANT_CONNECT_DB_ER = 2003


class ErrorHandling:

    # Error When Connecting To DB
    def database_errors(error: pymysql.Error):
        # Can't Connect to Database:
        if (error.args[0] == CANT_CONNECT_DB_ER) and ("Can't connect" in error.args[1]):
            raise falcon.HTTPInternalServerError("Error", "Can't Connect to Database")

        # Sleeping Database
        elif "Communications link failure" in error.args[1]:
            raise falcon.HTTPInternalServerError("Error", "Database Connection Failed - Check the DB is awake")
        # Other Error
        else:
            raise falcon.HTTPInternalServerError("Error", "Database Error")

    # Error When Processing Data
    def processing_errors(error: pymysql.Error):
        # to reduce information leakage - only report a bad request
        print(error)
        raise falcon.HTTPBadRequest("Bad Request", "Bad request")

