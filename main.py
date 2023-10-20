import uvicorn
import asyncio
from fastapi import FastAPI, Query
from gnews import get_data
from singlescrape import single_scrape
from similarity import assign_interest
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "YEM Crawl and Scrape"}


@app.get("/crawler/queryString/{queryString}")
async def link_collate(queryString):
    return get_data(queryString)


@app.get("/scraper")
async def scrape(url: str):
    try:
        result = await asyncio.wait_for(single_scrape(url), timeout=30)
        return result
    except asyncio.TimeoutError as e:
        return "SCRAPER TIMEOUT"


@app.get("/items/")
async def get_item(title: str, interests: List[str] = Query(...)):
    return assign_interest(title, interests)


if __name__ == "__main__":
    uvicorn.run("main:app")
