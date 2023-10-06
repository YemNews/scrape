from flask import Flask
from scrape import adv_scrape
from gnews import get_data

app = Flask(__name__)

@app.route('/')
def main(topics):
    return 'YEM Scrape'

@app.route('/links/<links>')
def link_collate(links):
    return get_data(links)

@app.route('/topic/<topic>')
def scrape_collate(topic):
    return adv_scrape(get_data(topic))

if __name__=="__main__":
    app.run(debug=True)