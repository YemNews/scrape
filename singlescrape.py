import newspaper
import csv
import requests
import logging

def single_scrape(link):
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


# print(single_scrape('https://news.google.com/rss/articles/CBMiTGh0dHBzOi8vaGl0Y29uc3VsdGFudC5uZXQvMjAyMy8xMC8wNi9oZWFsdGhjYXJlLWFpLXBoeXNpY2lhbi1idXJub3V0LWNyaXNpcy_SAQA?oc=5'))