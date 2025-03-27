from models import (
    model_products,
    model_product_details,
    model_product_reviews,
    model_product_brands,
)
from schemas import Filter
from typing import Annotated


def controller_products(filter: Filter):
    return model_products(filter)


def controller_product_details(id: int):
    return model_product_details(id)


def controller_product_review(id: int):
    return model_product_reviews(id)


def controller_product_brands():
    return model_product_brands()
