from sqlmodel import select
from models.db_mysql import mysql_sqlmodel
from schemas import DB_Users, DB_Reviews, DB_Products, DB_Orders, DB_SoldProducts
from schemas import User, UserReview, UserOrder, UserOrderDetails, OrderedProduct

# from schemas import User


@mysql_sqlmodel
def user(user_id: int, session) -> User:
    query = select(DB_Users).where(DB_Users.userId == user_id)
    result = session.exec(query).all()[0].model_dump()
    response = User(**result)
    print(response)

    return response


@mysql_sqlmodel
def user_reviews(user_id: int, session):
    query = (
        select(
            DB_Reviews.reviewId,
            DB_Products.productId,
            DB_Products.productName,
            DB_Reviews.reviewDate,
            DB_Users.userName,
            DB_Reviews.reviewDetails,
            DB_Reviews.rating,
        )
        .join(DB_Products, DB_Products.productId == DB_Reviews.productId)
        .join(DB_Users, DB_Users.userId == DB_Reviews.userId)
        .where(DB_Users.userId == user_id)
    )
    result = session.exec(query).all()
    response = []
    for i in result:
        response.append(
            {
                "reviewId": i[0],
                "productId": i[1],
                "productName": i[2],
                "reviewDate": i[3],
                "username": i[4],
                "review": i[5],
                "ratings": i[6],
            }
        )

    print(result)

    return response


@mysql_sqlmodel
def user_orders(user_id: int, session):
    query = select(DB_Orders).where(DB_Orders.userId == user_id)
    result = session.exec(query).all()
    response = []
    for i in result:
        response.append(UserOrder(**i.model_dump()))

    return response


@mysql_sqlmodel
def user_order_details(user_id, order_id: int, session):
    query = (
        select(DB_Orders)
        .where(DB_Orders.userId == user_id)
        .where(DB_Orders.orderId == order_id)
    )
    result = session.exec(query).all()

    product_query = (
        select(
            DB_SoldProducts.productId,
            DB_Products.productName,
            DB_SoldProducts.quantity,
            DB_SoldProducts.perCost,
            DB_SoldProducts.perDiscount,
            DB_SoldProducts.totalCost,
        )
        .join(DB_Products, DB_Products.productId == DB_SoldProducts.productId)
        .where(DB_SoldProducts.orderId == order_id)
    )

    db_products = session.exec(product_query).all()
    products = []
    for p in db_products:
        products.append(
            OrderedProduct(
                **{
                    "productId": p[0],
                    "productName": p[1],
                    "quantity": p[2],
                    "price": p[3],
                    "discount": p[4],
                    "total": p[5],
                }
            )
        )

    response = UserOrderDetails(**result[0].model_dump(), product=products)

    return response
