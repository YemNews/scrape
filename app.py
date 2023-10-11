from flask import Flask, request
from scrape import adv_scrape
from singlescrape import single_scrape
from gnews import get_data

app = Flask(__name__)

@app.route('/')
def main():
    return 'YEM Scrape'

@app.route('/crawler/topic/<topic>/interest/<interest>')
def link_collate(topic, interest):
    return get_data(topic, interest)

@app.route('/scraper', methods=['GET'])
def scrape():
    link = request.args.get('url')
    print(link)
    return single_scrape(link)

if __name__=="__main__":
    app.run(debug=True)


# Flow
# 1. Call the crawler for each interest-topic
# 2. Get articles for interest/topic combo
# 3. 
# news.google.com/rss/articles/CBMiTGh0dHBzOi8vaGl0Y29uc3VsdGFudC5uZXQvMjAyMy8xMC8wNi9oZWFsdGhjYXJlLWFpLXBoeXNpY2lhbi1idXJub3V0LWNyaXNpcy_SAQA?oc=5