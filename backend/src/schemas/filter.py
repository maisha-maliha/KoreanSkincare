from pydantic import BaseModel


class Filter(BaseModel):
    skin: list[int] = []
    concern: list[int] = []
    productType: list[int] = []
    offset: int = 0
    limit: int = 0
