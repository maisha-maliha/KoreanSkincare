from fastapi import APIRouter

# from controller import controller_user

router = APIRouter(prefix="/users", tags=["Users"])


# ============ GET ===============


# @router.get("/{user_id}")
# async def user(user_id: int):
#     return controller_user(user_id)


@router.get("/{user_id}/orders")
async def user_orders():
    pass


@router.get("/{user_id}/wishlist")
async def user_wishlist():
    pass


@router.get("/{user_id}/reviews")
async def user_review():
    pass


@router.get("/{user_id}/orders/{order_id}")
async def user_order_details():
    pass
