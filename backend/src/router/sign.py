from fastapi import APIRouter

router = APIRouter(prefix="/sign", tags=["Sign"])

# ============ POST ===============

@router.post("/in")
async def sign_in():
    pass

@router.post("/out")
async def sign_out():
    pass