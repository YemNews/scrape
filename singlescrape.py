import asyncio
import logging
import requests
import newspaper

logging.basicConfig(filename="mylogs.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

async def single_scrape(link):
    json_response = []
    # await asyncio.sleep(100)
    try:
        # Seperate breakdown timeout. Must be a lower value than 30. Max chance of failure.
        endpoint = await asyncio.wait_for(get_final_endpoint(link), timeout=15)
    except asyncio.TimeoutError:
        logger.error(f'Timeout occurred while fetching {link}')
        return json_response

    try:
        article = newspaper.Article(url=endpoint)
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
        logger.info(f'Link scraped')

    except:
        logger.error('Scraping error')

    return json_response


async def get_final_endpoint(link):

    r = await asyncio.get_event_loop().run_in_executor(None, requests.get, link)
    return r.url


# Getting the final endpoint - seperate timeout (30s) - max chance of failure!!
# Scraping that endpoint

# Overall 30 seconds