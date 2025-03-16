import mysql.connector as db
from models.config import USER, PASSWORD, DATABASE, HOST

database_config = {
    "user": USER,
    "password": PASSWORD,
    "host": HOST,
    "database": DATABASE,
}


def mysql_database_connection(func):
    def wrapper(*args, **kwargs):
        try:
            conn = db.connect(**database_config)
            cursor = conn.cursor()
            return func(*args, **kwargs, database=conn, cursor=cursor)
        except db.Error as err:
            print("database connection error: ", err)
        finally:
            cursor.close()
            conn.close()
        return None

    return wrapper


# =========== tried but gave error
# def database_connection(func):
#     def wrapper(*args, **kwargs):
#         try:
#             with db.connect(**database_config) as conn:
#                 with conn.cursor() as cursor:
#                     return func(*args, **kwargs, database=conn, cursor=cursor)
#         except db.Error as err:
#             print("database connection error: ", err)
#         return None

#     return wrapper
