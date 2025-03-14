from fastapi import APIRouter

router = APIRouter(prefix = "/users", tags=["Users"])


# ============ GET ===============

@router.get("/{user_id}")
async def user():
    pass

@router.get("/{user_id}/orders")
async def user_orders():
    pass

@router.get("/{user_id}/orders/{order_id}")
async def user_order_details():
    pass

@router.get("/{user_id}/wishlist")
async def user_wishlist():
    pass

@router.get("/{user_id}/reviews")
async def user_review():
    pass