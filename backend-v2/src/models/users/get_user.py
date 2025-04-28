from models.db_mysql import mysql_database_connection
from schemas import User


@mysql_database_connection
def user(user_id: int, database, cursor) -> User:
    query = f"SELECT * FROM users WHERE userId = {user_id}"
    cursor.execute(query)
    result = list(cursor.fetchone())
    column = list(User.model_fields.keys())
    data = dict(zip(column, result))
    user_data = User(**data)
    return user_data


@mysql_database_connection
def user_orders(user_id: int, database, cursor):
    pass


@mysql_database_connection
def user_order_id(order_id: int, database, cursor):
    pass
