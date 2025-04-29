from fastapi import APIRouter
from controller import (
    controller_user,
    controller_user_order,
    controller_user_order_details,
    controller_user_review,
)

# from controller import controller_user

router = APIRouter(prefix="/users", tags=["Users"])


# ============ GET ===============


@router.get("/{user_id}")
async def user(user_id: int):
    return controller_user(user_id)


@router.get("/{user_id}/orders")
async def user_orders(user_id: int):
    return controller_user_order(user_id)


@router.get("/{user_id}/reviews")
async def user_review(user_id: int):
    return controller_user_review(user_id)


@router.get("/{user_id}/orders/{order_id}")
async def user_order_details(user_id: int, order_id: int):
    return controller_user_order_details(user_id, order_id)
