from pydantic import BaseModel


class Products(BaseModel):
    productId: int
    productName: str
    brandName: str
    price: int
    discount: int
    productVisibility: int
    averageRating: float
    totalRating: int


class ProductDetails(BaseModel):
    productId: int
    productName: str
    brandId: int
    brandName: str
    price: int
    discount: int
    productVisibility: int
    averageRating: float
    totalRating: int
    details: str
    skin: list[list]
    concern: list[list]
    productType: list[list]
    ingredients: list[list]


class ProductReviews(BaseModel):
    reviewId: int
    username: str
    review: str
    ratings: float


class Brand(BaseModel):
    brandId: int
    brandName: str
    visibility: int = 1
