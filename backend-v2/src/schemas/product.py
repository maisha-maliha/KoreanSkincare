from pydantic import BaseModel


class Products(BaseModel):
    productId: int
    productName: str
    brandName: str
    price: int
    discount: int
    visibility: int
    averageRating: float
    totalRating: int


class ProductDetails(BaseModel):
    productId: int
    productName: str
    brandId: int
    brandName: str
    price: int
    discount: int
    visibility: int
    averageRating: float
    totalRating: int
    details: str
    skin: list[dict]
    concern: list[dict]
    productType: list[dict]
    ingredients: list[dict]


class ProductReviews(BaseModel):
    reviewId: int
    username: str
    review: str
    ratings: float


class Brand(BaseModel):
    brandId: int
    brandName: str
    visibility: int = 1
