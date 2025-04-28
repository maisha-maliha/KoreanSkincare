from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

# ============ GET ===============

@router.get("/{admin_id}")
async def admin_profile():
    pass

@router.get("/{admin_id}/brand")
async def admin_brands():
    pass

@router.get("/{admin_id}/brand/{brand_id}")
async def admin_brand_id():
    pass

# ============ POST ===============

@router.post("/")
async def admin_login():
    pass

