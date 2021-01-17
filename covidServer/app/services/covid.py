from ..models.request import Country
from ..models.response import CountryTests, MonthlyTests
import pandas as pd
from iso3166 import countries

COVID19_DATA_FILE = "./app/data/monthly_covid_testing_data.csv"
COUNTRIES = "Denmark", "Germany", "Romania", "Spain", "Sweden"


async def read_covid_data(country: Country) -> CountryTests:
    df = pd.read_csv(COVID19_DATA_FILE)
    df = df[df.country_code == country.country]
    tests = [MonthlyTests(month=row.month, tests=row.tests_done) for row in df.itertuples()]
    return CountryTests(country_code=country.country, tests=tests)


async def check_country_iso_code(country: Country) -> bool:
    relevant = list(filter(lambda c: c.name in COUNTRIES, countries))
    alpha2 = list(map(lambda c: c.alpha2, relevant))
    b = country.country in alpha2
    return b
