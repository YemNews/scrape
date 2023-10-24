import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gnews import get_data
from singlescrape import single_scrape

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods or be specific e.g., ["GET", "POST"]
    allow_headers=["*"],  # Allow all headers or be specific e.g., ["Content-Type"]
)

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


# @app.get("/items/")
# async def get_item(title: str, interests: List[str] = Query(...)):
#     return assign_interest(title, interests)


if __name__ == "__main__":
    uvicorn.run("main:app")
