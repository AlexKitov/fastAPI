from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str = Field(default='DK', example='DK')

