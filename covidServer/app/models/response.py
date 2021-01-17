from pydantic import BaseModel


class MonthlyTests(BaseModel):
    month: str
    tests: int


class CountryTests(BaseModel):
    country_code: str
    tests: list

