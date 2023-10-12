from pygooglenews import GoogleNews
from langdetect import detect

def get_data(topic, curr_interest):
    gn = GoogleNews()
    negate_interests_query = 'New Regulations'
    s = gn.search(f'{topic} {curr_interest} -Regulations', when='24h')
    data = []
    for entry in s["entries"]:
        item = {
            "title" : entry["title"],
            "link": entry["link"],
            "published": entry["published"],
            "source": entry["source"]["title"],
        }
        if detect(item["title"]) == 'en':
            data.append(item)
    return data

data = get_data("Generative AI","New Startups")
print(len(data))
for item in data:
    print(item['title'])

