from fastapi import APIRouter, HTTPException
from ..models.request import Country
from ..models.response import CountryTests

from ..services import covid

router = APIRouter(
    prefix="/country_tests_done",
    tags=["covid"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def country_tests_done(country: Country) -> CountryTests:
    if not await covid.check_country_iso_code(country):
        raise HTTPException(status_code=404, detail=f"Item '{country.country}' not found")
    return await covid.read_covid_data(country)
