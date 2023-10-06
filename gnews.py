from pygooglenews import GoogleNews
from langdetect import detect

def get_data(topic, interest):
    gn = GoogleNews()
    s = gn.search(f'{topic} {interest}', when='1h')
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

# print(get_data("Generative AI"))

