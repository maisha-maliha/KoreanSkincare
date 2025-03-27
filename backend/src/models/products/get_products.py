from models.db_mysql import mysql_database_connection
from schemas import Products, Filter, ProductDetails, ProductReviews, Brand


@mysql_database_connection
def products(filter: Filter, database, cursor) -> list[Products]:
    query_selectors = """
    SELECT 
    products.productId, 
    products.productName, 
    brands.brandName, 
    products.price, 
    products.discount, 
    products.visibility, 
    products .averageRating,
    products.totalRating 
    """
    query_joins = """
    FROM products
    INNER JOIN brands 
    ON products.brandId = brands.brandId
    """
    query_condition = """
    WHERE brands.visibility = 1
    """
    # ==== ALL CONDITIONS ========
    if filter.skin:
        query_joins += "INNER JOIN productSkin ON products.productId = productSkin.ProductId INNER JOIN skin ON productSkin.skinId = skin.SkinId"
        skin_ids = ",".join(
            map(str, filter.skin)
        )  # Convert list to comma-separated string
        query_condition += f" AND skin.skinId IN ({skin_ids})"

    if filter.concern:
        query_joins += "INNER JOIN productConcerns ON products.productId = productConcerns.ProductId INNER JOIN concerns ON productConcerns.concernId = concerns.concernId"
        concern_ids = ",".join(
            map(str, filter.concern)
        )  # Convert list to comma-separated string
        query_condition += f" AND concerns.concernId IN ({concern_ids})"

    if filter.productType:
        query_joins += "INNER JOIN productProductType ON products.productId = productProductType.ProductId INNER JOIN productType ON productType.typeId = productProductType.productTypeId"
        product_type_ids = ",".join(
            map(str, filter.productType)
        )  # Convert list to comma-separated string
        query_condition += f" AND productType.typeId IN ({product_type_ids})"

    if filter.brand:
        query_condition += f" AND brands.brandId = {filter.brand}"

    if filter.onSale:
        query_condition += " AND products.discount > 0"

    if filter.limit:
        query_condition += f" LIMIT {filter.limit}"

    if filter.offset:
        query_condition += f" OFFSET {filter.offset}"

    # form whole query
    query = query_selectors + query_joins + query_condition
    print("\n\n", query, "\n\n")
    # execute the query
    cursor.execute(query)
    # query result return
    products_list: list[Products] = []
    # create products list
    for p in cursor.fetchall():
        columns = list(Products.model_fields.keys())
        item_data = dict(zip(columns, p))  # Convert tuple to dictionary
        item = Products(**item_data)  # Pass as keyword arguments
        products_list.append(item)

    return products_list


@mysql_database_connection
def product_details(id, database, cursor) -> ProductDetails:
    query = f"""
    SELECT products.productId, 
    products.productName, 
    products.brandId, 
    brands.brandName, 
    products.price,
    products.discount,
    products.visibility,
    products.averageRating,
    products.totalRating,
    products.details
    FROM products
    INNER JOIN brands ON products.brandId = brands.brandId
    WHERE products.productId = {id};
    """
    cursor.execute(query)
    row = cursor.fetchone()

    result = list(row)
    result.append(product_skin_types(id))
    result.append(product_concerns(id))
    result.append(product_type(id))
    result.append(product_ingredients(id))

    columns = list(ProductDetails.model_fields.keys())
    item_data = dict(zip(columns, result))

    return ProductDetails(**item_data)


@mysql_database_connection
def product_review(id, database, cursor) -> list[ProductReviews]:
    query = f"""
    SELECT reviews.reviewId,
    users.userName,
    reviews.reviewDetails,
    reviews.rating
    FROM reviews
    INNER JOIN users ON users.userId = reviews.userId
    WHERE reviews.productId ={id}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    # query result return
    reviews_list: list[ProductReviews] = []
    # create reviews list
    for p in result:
        columns = list(ProductReviews.model_fields.keys())
        item_data = dict(zip(columns, p))  # Convert tuple to dictionary
        item = ProductReviews(**item_data)  # Pass as keyword arguments
        reviews_list.append(item)
    return reviews_list


@mysql_database_connection
def product_ingredients(id, database, cursor):
    query = f"""
    SELECT ingredients.ingredientId, ingredients.ingredientName
    FROM ingredients
    INNER JOIN productIngredients ON ingredients.ingredientId = productIngredients.ingredientId
    WHERE productId = {id}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return list(result)


@mysql_database_connection
def product_skin_types(id, database, cursor):
    query = f"""
    SELECT skin.skinId, skin.skinName
    FROM Skin
    INNER JOIN productSkin ON skin.SkinId = productSkin.skinId
    WHERE productId = {id}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return list(result)


@mysql_database_connection
def product_concerns(id, database, cursor):
    query = f"""
    SELECT concerns.concernId, concerns.concern
    FROM concerns
    INNER JOIN productConcerns ON concerns.concernId = productConcerns.concernId
    WHERE productId = {id}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return list(result)


@mysql_database_connection
def product_type(id, database, cursor):
    query = f"""
    SELECT productType.typeId, 
    productType.typeName 
    FROM productProductType 
    INNER JOIN productType ON productProductType.productTypeId = productType.typeId
    WHERE productId = {id}
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return list(result)


@mysql_database_connection
def product_brands(database, cursor) -> list[Brand]:
    query = "SELECT * FROM brands"
    cursor.execute(query)
    result = cursor.fetchall()
    brands_list: list[Brand] = []
    for b in result:
        columns = list(Brand.model_fields.keys())
        item = dict(zip(columns, [b[0], b[1], b[2]]))
        brands_list.append(Brand(**item))
    return brands_list
