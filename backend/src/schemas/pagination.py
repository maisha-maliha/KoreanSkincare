from pydantic import BaseModel, Field

class Pagination(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(100, gt=0, le=100)