
import logging

import updatedscrape.newspaper as legendscrape

logging.basicConfig(
    filename="mylogs.log", format="%(asctime)s %(message)s", filemode="w"
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


async def single_scrape(link):
    json_response = []
    try:
        article = legendscrape.Article(url=link)
        article.download()
        article.parse()

        curr_article = {
            "title": article.title,
            "text": article.text,
            "publishedDate": article.publish_date,
            "image": article.top_image,
        }

        json_response.append(curr_article)
        logger.info(f"Link scraped: {article.title}")

    except Exception as e:
        logger.error(f"Scraping error for {link}: {str(e)}")

    return json_response
