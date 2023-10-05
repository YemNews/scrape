import newspaper
import csv
import requests
import logging
from datetime import timedelta
from gnews import get_data
# from simplescraper import simple_scrape



def adv_scrape(data):
    logging.basicConfig(filename="mylogs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    dump = {}
    with open ('scraper_requests_adv.csv', 'w+') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['title','link','published','source','text']
        csvwriter.writerow(fields)
        i = 0
        for item in data:
            try:
                endpoint = get_final_endpoint(item['link'])
            except:
                logger.error(f'Error fetching {item["link"]}')
                continue

            try:
                article = newspaper.Article(url=endpoint)
                article.download()
                article.parse()
            except:
                logger.error('Scraping error')
                continue

            article ={
                "title": str(article.title),
                "text": str(article.text)
            }
            content = [item["title"], endpoint, item["published"], item["source"], article["text"]]
            csvwriter.writerow(content)
            dump[f'article {i}'] = content
            logger.info(f'Row written')
            i += 1
    return str(dump)
# def basic_scrape(data):
#     with open ('printing_packaging.csv','w+') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         fields = ['title','link','published','source','text']
#         csvwriter.writerow(fields)
#         for item in data:
#             try:
#                 endpoint = get_final_endpoint(item['link'])
#             except:
#                 logger.error(f'Error fetching {item["link"]}')

#             content = [item["title"], endpoint, item["published"], item["source"]]
            
#             try:
#                 text = simple_scrape(endpoint)
#             except:
#                 logger.error('Scraping error')
#                 continue

#             content.append(text)
#             print(content)
#             csvwriter.writerow(content)

def get_final_endpoint(link):
    r = requests.get(link)
    return r.url 

# start = time.time()
# dump = adv_scrape(get_data("Generative AI"))
# end = time.time()

# print(str(timedelta(seconds=end-start)))

# with open ('dict.txt', 'w+') as f:
#     f.write(str(dump))