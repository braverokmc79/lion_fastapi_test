from typing import Annotated
from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/search/")
async def search_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50, description="")] = None

):
    return {"q": q}