from models.db_mysql import mysql_database_connection
from models.db_mongoDB import mongodb_database_connection
from schemas import Filter


@mysql_database_connection
def product(id, database, cursor) -> list[dict]:
    query = """
    SELECT 
        products.productId, 
        products.productName, 
        brands.brandName, 
        products.price, 
        products.discount, 
        products.visibility as productVisibility
    FROM products 
    INNER JOIN brands ON products.brandId = brands.brandId
    WHERE brands.visibility = 1 AND productId = %s
    ;"""
    cursor.execute(query, (id,))
    product: list[dict] = []
    products = cursor.fetchall()
    product.append(
        {
            "productId": product[0],
            "productName": product[1],
            "brandId": product[2],
            "brandName": product[3],
            "price": product[4],
            "discount": product[5],
            "productVisibility": product[6],
        }
    )
    return product


@mongodb_database_connection
def filtered_products(data: Filter, collection):
    filter_query = {}
    if data.skin:
        filter_query.update({"skinId": {"$all": data.skin}})
    if data.concern:
        filter_query.update({"concernId": {"$all": data.concern}})
    if data.productType:
        filter_query.update({"typeId": {"$all": data.productType}})
    print(filter_query)
    products: list[dict] = list(
        collection.find(filter_query, {"_id": 0}).skip(data.offset).limit(data.limit)
    )
    return products
