from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str =Field(min_length=2)
    pages: int = Field(gt=0)