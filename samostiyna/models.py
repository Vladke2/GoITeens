from pydantic import BaseModel, Field, field_validator
from typing import Optional
from typing import Any


class User(BaseModel):
    id: int
    name: str = Field(..., gt=2, le=50)
    email: str
    age: Optional[int] = Field(None, gt=18, le=100)

    @field_validator("age")
    @classmethod
    def check_age(cls, value: Any):
        if value is not None:
            if value <= 18:
                raise ValueError('need > 18')
            if value >= 100:
                raise ValueError('need < 100')
        return value


class Item(BaseModel):
    id: int
    title: str = Field(..., gt=2, le=100)
    description: Optional[str] = Field(..., le=500)
    price: float = Field(..., gt=0)

    @field_validator(price)
    @classmethod
    def check_price(cls, value: Any):
        if value > 0:
            return value
        raise ValueError('need > 0')
