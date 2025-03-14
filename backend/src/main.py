from fastapi import FastAPI, APIRouter
from router import users_router, products_router, admin_router, sign_router

app = FastAPI()

# include all routes
app.include_router(users_router)
app.include_router(products_router)
app.include_router(admin_router)
app.include_router(sign_router)