from pydantic import BaseModel

class Filter(BaseModel):
    skin: list[str] = None
    concern: list[str] = None
    product: list[str] = None