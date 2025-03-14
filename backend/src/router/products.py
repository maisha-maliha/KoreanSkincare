from fastapi import APIRouter

router = APIRouter(prefix = "/products", tags=["Products"])


# ============ GET ===============

@router.get("/")
async def products():
    pass

@router.get("/{product_id}")
async def product_id():
    pass

@router.get("/{product_id}/reviews-ratings")
async def product_review_rating():
    pass

@router.get("/onsale")
async def products_onsale():
    pass

@router.get("/new")
async def products_new():
    pass

@router.get("/brand/{brand_id}")
async def products():
    pass

