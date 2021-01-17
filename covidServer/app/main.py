from fastapi import FastAPI

from .routers import covid

app = FastAPI()

app.include_router(covid.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
