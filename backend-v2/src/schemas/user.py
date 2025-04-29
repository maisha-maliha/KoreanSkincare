from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class User(BaseModel):
    userId: int
    createdTime: datetime
    userName: str
    email: EmailStr
    age: date
    userPassword: str
    phone: int
    address: str | None = None


class UserReview(BaseModel):
    reviewId: int
    productId: int
    productName: str
    reviewDate: datetime
    username: str
    review: str
    ratings: float


class UserOrder(BaseModel):
    orderId: int
    userId: int
    orderDate: datetime
    discount: int
    totalPaid: int
    address: str
    paymentMethod: int


class OrderedProduct(BaseModel):
    productId: int
    productName: str
    quantity: int
    price: int
    discount: int
    total: int


class UserOrderDetails(BaseModel):
    orderId: int
    product: list[OrderedProduct]
    orderDate: datetime
    totalPaid: int
    address: str
    paymentMethod: int
