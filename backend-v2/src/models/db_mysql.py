from sqlmodel import create_engine, Session
from functools import wraps
import mysql.connector as db
import os
from dotenv import load_dotenv

# laoding all .env data
load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")


database_config = {
    "user": USER,
    "password": PASSWORD,
    "host": HOST,
    "database": DATABASE,
}

database_url = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
connection = create_engine(database_url, echo=True)

from functools import wraps


def mysql_database_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        cursor = None
        try:
            conn = db.connect(**database_config)
            cursor = conn.cursor()
            print("Database connection opened ======")
            result = func(*args, **kwargs, database=conn, cursor=cursor)
            conn.commit()  # optional, if you modify database
            return result
        except db.Error as err:
            print("Database connection error: ", err)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            print("Database connection closed ======")

    return wrapper


def mysql_sqlmodel(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = None
        try:
            session = Session(connection)
            print("SQLModel Session opened =======")
            result = func(*args, **kwargs, session=session)
            session.commit()  # commit transaction if needed
            return result
        except Exception as e:
            print("SQLModel session error: ", e)
            if session:
                session.rollback()
        finally:
            if session:
                session.close()
            print("SQLModel Session closed =======")

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
