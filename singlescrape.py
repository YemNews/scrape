import newspaper
import csv
import requests
import logging
import time
from wrapt_timeout_decorator import *

@timeout(dec_timeout=30, exception_message='Scraper timeout')
def single_scrape(link):
    # Uncomment line 11 to check if it works on your machine
    # time.sleep(50)
    logging.basicConfig(filename="mylogs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    json_response = []

    try:
        endpoint = get_final_endpoint(link)
    except:
                logger.error(f'Error fetching {link}')

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


def get_final_endpoint(link):
    r = requests.get(link)
    return r.url 



#===========SETUP AND TRY IN YOUR MACHINE==============
# pip install wrapt_timeout_decorator (inside env)

# CODE BELOW FOR CHECKING IF IT WORKS
# if __name__ ==  '__main__':
#     try:
#         print(single_scrape(link='https://www.thehindu.com/news/international/magnitude-63-earthquake-strikes-northwestern-afghanistan/article67406480.ece'))
#     except TimeoutError as e:
#         print(e)

# NOTE: Add dec_timeout=x parameter to func call to override 30 seconds default