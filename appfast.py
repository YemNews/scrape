import uvicorn
import asyncio
from fastapi import FastAPI, BackgroundTasks
from gnews import get_data
from singlescrape import single_scrape

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "YEM Crawl and Scrape"}

@app.get('/crawler/topic/{topic}/interest/{interest}')
async def link_collate(topic, interest):
    return get_data(topic, interest)

@app.get('/scraper')
async def scrape(url: str):
    try:
        result = await asyncio.wait_for(single_scrape(url), timeout=30)
        return result
    except asyncio.TimeoutError as e:
        return 'SCRAPER TIMEOUT'
 
if __name__ == "__main__":
    uvicorn.run("appfast:app")