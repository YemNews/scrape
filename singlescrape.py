import asyncio
import logging
import requests
import newspaper

logging.basicConfig(filename="mylogs.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

async def single_scrape(link):
    json_response = []
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
        article.nlp()  # This line will calculate the summary and keywords
        
        curr_article = {
            "title": article.title,
            "text": article.text,
            "summary": article.summary,  # This line will get the summary
            "keywords": article.keywords  # This line will get the keywords
        }

        json_response.append(curr_article)
        logger.info(f'Link scraped: {article.title}')

    except Exception as e:
        logger.error(f'Scraping error for {link}: {str(e)}')

    return json_response

async def get_final_endpoint(link):
    r = await asyncio.get_event_loop().run_in_executor(None, requests.get, link)
    return r.url
