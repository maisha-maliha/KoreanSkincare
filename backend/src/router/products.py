from fastapi import APIRouter, Path, Query
from typing import Annotated
from schemas import Filter

from controller import product, products_filtered

router = APIRouter(prefix="/products", tags=["Products"])


# ============ GET ===============


@router.get("/")
async def products(filter: Annotated[Filter, Query()]):
    """get all products"""
    return products_filtered(filter)


@router.get("/{id}")
async def product_id(id: Annotated[int, Path()]):
    """get a certain product information"""
    return product(id)


@router.get("/{product_id}/reviews-ratings")
async def product_review_rating():
    """get all reviews and ratings of a certain product"""
    pass


@router.get("/onsale")
async def products_onsale():
    """get all products that has discount"""
    pass


@router.get("/new")
async def products_new():
    """get the latest added products"""
    pass


@router.get("/brands}")
async def brands():
    """get list of all brands"""
    pass


@router.get("/brands/{brand_id}")
async def brand_id():
    """get all products of a brand"""
    pass
