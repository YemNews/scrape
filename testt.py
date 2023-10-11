from fastapi import FastAPI
import asyncio
app = FastAPI()

async def single_scrape(link):
    json_response = []
    # await asyncio.sleep(10)
    try:
        article = newspaper.Article(url=link)
        article.download()
        article.parse()

        article = {
            "title": str(article.title),
            "text": str(article.text)
        }
        curr_article = {
            "text": article["text"]
        }

        json_response.append(curr_article)
        # logger.info(f'Link scraped')

    except:
        print('Scraping error')

    return json_response

@app.get("/scrape_with_timeout")
async def scrape_with_timeout(link: str):
    timeout_seconds = 10  # Set your desired timeout

    try:
        result = await asyncio.wait_for(single_scrape(link), timeout_seconds)
        return result
    except asyncio.TimeoutError:
        return {"message": "Scraping operation timed out"}

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    import newspaper
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
