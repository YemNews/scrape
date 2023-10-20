import asyncio
import logging
import requests
import newspaper

logging.basicConfig(
    filename="mylogs.log", format="%(asctime)s %(message)s", filemode="w"
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


async def single_scrape(link):
    json_response = []
    try:
        article = newspaper.Article(url=link)
        article.download()
        article.parse()  # This line will calculate the summary and keywords

        curr_article = {
            "title": article.title,
            "text": article.text,
            "summary": article.summary,  # This line will get the summary
            "keywords": article.keywords,  # This line will get the keywords
        }

        json_response.append(curr_article)
        print(json_response)
        logger.info(f"Link scraped: {article.title}")

    except Exception as e:
        logger.error(f"Scraping error for {link}: {str(e)}")

    return json_response
