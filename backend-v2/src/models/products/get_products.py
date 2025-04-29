from sqlmodel import select
from models.db_mysql import mysql_database_connection, mysql_sqlmodel
from schemas import Products, Filter, ProductDetails, ProductReviews, Brand
from schemas import (
    DB_Admins,
    DB_Brands,
    DB_Concerns,
    DB_Ingredients,
    DB_Orders,
    DB_Inventory,
    DB_PaymentMethods,
    DB_ProductConcerns,
    DB_ProductIngredients,
    DB_ProductProductType,
    DB_Products,
    DB_ProductSkin,
    DB_ProductType,
    DB_Reviews,
    DB_Skin,
    DB_SoldProducts,
    DB_Users,
)


@mysql_sqlmodel
def all_products(filter: Filter, session) -> list[Products]:
    query = select(
        DB_Products.productId,
        DB_Products.productName,
        DB_Brands.brandName,
        DB_Products.price,
        DB_Products.discount,
        DB_Products.visibility,
        DB_Products.averageRating,
        DB_Products.totalRating,
    ).join(DB_Brands, DB_Products.brandId == DB_Brands.brandId)

    if filter.skin:
        query = query.join(
            DB_ProductSkin, DB_ProductSkin.productId == DB_Products.productId
        ).where(DB_ProductSkin.skinId.in_(filter.skin))
    if filter.concern:
        query = query.join(
            DB_ProductConcerns, DB_ProductConcerns.productId == DB_Products.productId
        ).where(DB_ProductConcerns.concernId.in_(filter.concern))
    if filter.productType:
        query = query.join(
            DB_ProductProductType,
            DB_ProductProductType.productId == DB_Products.productId,
        ).where(DB_ProductProductType.productTypeId.in_(filter.productType))
    if filter.offset:
        query = query.where(DB_Products.productId >= filter.offset)
    if filter.limit:
        query = query.limit(filter.limit)

    result = session.exec(query).all()
    response = []
    for p in result:
        product_info = {
            "productId": p[0],
            "productName": p[1],
            "brandName": p[2],
            "price": p[3],
            "discount": p[4],
            "visibility": p[5],
            "averageRating": p[6],
            "totalRating": p[7],
        }

        response.append(Products(**product_info))

    return response


@mysql_sqlmodel
def product_details(id, session) -> ProductDetails:
    product_statement = (
        select(
            DB_Products.productId,
            DB_Products.productName,
            DB_Brands.brandId,
            DB_Brands.brandName,
            DB_Products.price,
            DB_Products.discount,
            DB_Products.visibility,
            DB_Products.averageRating,
            DB_Products.totalRating,
            DB_Products.details,
        )
        .join(DB_Brands, DB_Products.brandId == DB_Brands.brandId)
        .where(DB_Products.productId == id)
    )
    skin_statement = (
        select(DB_Skin.skinId, DB_Skin.skinName)
        .join(DB_ProductSkin, DB_Skin.skinId == DB_ProductSkin.skinId)
        .where(DB_ProductSkin.productId == id)
    )
    concern_statement = (
        select(DB_Concerns.concernId, DB_Concerns.concern)
        .join(DB_ProductConcerns, DB_ProductConcerns.concernId == DB_Concerns.concernId)
        .where(DB_ProductConcerns.productId == id)
    )
    ingredient_statement = (
        select(DB_Ingredients.ingredientId, DB_Ingredients.ingredientName)
        .join(
            DB_ProductIngredients,
            DB_ProductIngredients.ingredientId == DB_Ingredients.ingredientId,
        )
        .where(DB_ProductIngredients.productId == id)
    )
    type_statment = (
        select(DB_ProductType.typeId, DB_ProductType.typeName)
        .join(
            DB_ProductProductType,
            DB_ProductType.typeId == DB_ProductProductType.productTypeId,
        )
        .where(DB_ProductProductType.productId == id)
    )
    product = list(session.exec(product_statement).all()[0])
    concern = [
        {"concernId": row.concernId, "concern": row.concern}
        for row in session.exec(concern_statement).all()
    ]
    ingredients = [
        {"ingredientId": row.ingredientId, "ingredientName": row.ingredientName}
        for row in session.exec(ingredient_statement).all()
    ]
    product_type = [
        {"ingredientId": row.typeId, "ingredientName": row.typeName}
        for row in session.exec(type_statment).all()
    ]
    skin = [
        {"skinId": row.skinId, "skinName": row.skinName}
        for row in session.exec(skin_statement).all()
    ]
    result = ProductDetails(
        productId=product[0],
        productName=product[1],
        brandId=product[2],
        brandName=product[3],
        price=product[4],
        discount=product[5],
        visibility=product[6],
        averageRating=product[7],
        totalRating=product[8],
        details=product[9],
        skin=list(tuple(skin)),
        concern=list(tuple(concern)),
        productType=list(tuple(product_type)),
        ingredients=list(tuple(ingredients)),
    )

    return result


@mysql_sqlmodel
def product_review(id, session) -> list[ProductReviews]:
    query = (
        select(
            DB_Reviews.reviewId,
            DB_Users.userName,
            DB_Reviews.reviewDetails,
            DB_Reviews.rating,
        )
        .join(DB_Users, DB_Reviews.userId == DB_Users.userId)
        .where(DB_Reviews.productId == id)
    )
    result = session.exec(query).all()
    response = []
    for review in result:
        response.append(
            ProductReviews(
                reviewId=review[0],
                username=review[1],
                review=review[2],
                ratings=review[3],
            )
        )

    return response


@mysql_sqlmodel
def product_brands(session) -> list[Brand]:
    query = select(DB_Brands)
    brands = []
    for brand in session.exec(query).all():
        brands.append(
            Brand(
                brandId=brand.brandId,
                brandName=brand.brandName,
                visibility=brand.visibility,
            )
        )
    return brands


@mysql_sqlmodel
def product_skin_types(session) -> list[dict]:
    query = select(DB_Skin)
    result = []
    for s in session.exec(query).all():
        result.append({"skinId": s.skinId, "skinName": s.skinName})

    return result


@mysql_sqlmodel
def product_concerns(session):
    query = select(DB_Concerns)
    result = []
    for s in session.exec(query).all():
        result.append({"concernId": s.concernId, "concern": s.concern})

    return result


@mysql_sqlmodel
def product_types(session):
    query = select(DB_ProductType)
    result = []
    for s in session.exec(query).all():
        result.append({"typeId": s.typeId, "typeName": s.typeName})

    return result
