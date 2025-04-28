from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class User(BaseModel):
    userId: int
    createTime: datetime
    userName: str
    address: str
    email: EmailStr
    age: date
    userPassword: str
    phone: int
