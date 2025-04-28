from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from sqlalchemy import String
from datetime import datetime, date


# ------------------------------
# Admins Table
class DB_Admins(SQLModel, table=True):
    __tablename__ = "admins"

    adminId: int | None = Field(default=None, primary_key=True)
    adminName: str = Field(sa_column=String(50))
    email: EmailStr = Field(
        sa_column=String(50), sa_column_kwargs={"nullable": False, "unique": True}
    )
    adminPassword: str = Field(sa_column=String(120))
    adminRole: str = Field(sa_column=String(30))


# ------------------------------
# Brands Table
class DB_Brands(SQLModel, table=True):
    __tablename__ = "brands"

    brandId: int | None = Field(default=None, primary_key=True)
    brandName: str = Field(sa_column=String(80))
    visibility: int


# ------------------------------
# Products Table
class DB_Products(SQLModel, table=True):
    __tablename__ = "products"

    productId: int | None = Field(default=None, primary_key=True)
    productName: str = Field(sa_column=String(100))
    details: str = Field(sa_column=String(225))
    brandId: int
    price: int
    discount: int
    visibility: int
    averageRating: float
    totalRating: int


# ------------------------------
# Product Type Table
class DB_ProductType(SQLModel, table=True):
    __tablename__ = "producttype"

    typeId: int | None = Field(default=None, primary_key=True)
    typeName: str = Field(sa_column=String(30))


# ------------------------------
# Ingredients Table
class DB_Ingredients(SQLModel, table=True):
    __tablename__ = "ingredients"

    ingredientId: int | None = Field(default=None, primary_key=True)
    ingredientName: str = Field(sa_column=String(50))


# ------------------------------
# Skin Table
class DB_Skin(SQLModel, table=True):
    __tablename__ = "skin"

    skinId: int | None = Field(default=None, primary_key=True)
    skinName: str = Field(sa_column=String(50))


# ------------------------------
# Concerns Table
class DB_Concerns(SQLModel, table=True):
    __tablename__ = "concerns"

    concernId: int | None = Field(default=None, primary_key=True)
    concern: str = Field(sa_column=String(20))


# ------------------------------
# Reviews Table
class DB_Reviews(SQLModel, table=True):
    __tablename__ = "reviews"

    reviewId: int | None = Field(default=None, primary_key=True)
    userId: int
    productId: int
    reviewDate: datetime
    rating: int
    reviewDetails: str = Field(sa_column=String(255))


# ------------------------------
# Users Table
class DB_Users(SQLModel, table=True):
    __tablename__ = "users"

    userId: int | None = Field(default=None, primary_key=True)
    createdTime: datetime
    userName: str = Field(sa_column=String(50))
    address: str = Field(sa_column=String(120))
    email: EmailStr = Field(
        sa_column=String(50), sa_column_kwargs={"nullable": False, "unique": True}
    )
    phone: str = Field(sa_column=String(20))
    age: date
    userPassword: str = Field(sa_column=String(120))


# ------------------------------
# Inventory Table
class DB_Inventory(SQLModel, table=True):
    __tablename__ = "inventory"

    inventoryId: int | None = Field(default=None, primary_key=True)
    productId: int
    quantity: int


# ------------------------------
# Orders Table
class DB_Orders(SQLModel, table=True):
    __tablename__ = "orders"

    orderId: int | None = Field(default=None, primary_key=True)
    userId: int
    orderDate: datetime
    deliveryDate: datetime
    discount: int
    totalPaid: int
    address: str = Field(sa_column=String(120))
    paymentMethod: int


# ------------------------------
# Sold Products Table
class DB_SoldProducts(SQLModel, table=True):
    __tablename__ = "soldproducts"

    orderId: int
    productId: int
    quantity: int
    perCost: int
    perDiscount: int
    totalCost: int


# ------------------------------
# Payment Methods Table
class DB_PaymentMethods(SQLModel, table=True):
    __tablename__ = "paymentmethods"

    methodId: int | None = Field(default=None, primary_key=True)
    methodName: str = Field(sa_column=String(50))


# ------------------------------
# productIngredients Table
class DB_ProductIngredients(SQLModel, table=True):
    __tablename__ = "productingredients"

    productId: int
    ingredientId: int


# ------------------------------
# productSkin Table
class DB_ProductSkin(SQLModel, table=True):
    __tablename__ = "productskin"

    productId: int
    skinId: int


# ------------------------------
# productConcerns Table
class DB_ProductConcerns(SQLModel, table=True):
    __tablename__ = "productconcerns"

    productId: int
    concernId: int


# ------------------------------
# productProductType Table
class DB_ProductProductType(SQLModel, table=True):
    __tablename__ = "productproducttype"

    productId: int
    productTypeId: int
