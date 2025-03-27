from fastapi import APIRouter, Path, Query
from typing import Annotated
from schemas import Filter
from controller import (
    controller_products,
    controller_product_details,
    controller_product_review,
    controller_product_brands,
)


router = APIRouter(prefix="/products", tags=["Products"])


# ============ GET ===============


@router.get("/")
def products(filter: Annotated[Filter, Query()]):
    """get all products with any filter"""
    return controller_products(filter)


@router.get("/brands")
def brands():
    """get list of all brands"""
    return controller_product_brands()


@router.get("/{id}")
def product_id(id: Annotated[int, Path()]):
    """get a certain product information"""
    return controller_product_details(id)


@router.get("/{product_id}/reviews-ratings")
def product_review_rating(product_id: int):
    """get all reviews and ratings of a certain product"""
    return controller_product_review(product_id)
