from customscrape import GoogleNews
from langdetect import detect
from tryquickfetch import main


def timed(fnc):
    from functools import wraps
    import time

    @wraps(fnc)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fnc(*args, **kwargs)
        end = time.time()
        arg_str = ",".join(
            [str(arg) for arg in args] + ["{0}={1}".format(k, v) for (k, v) in kwargs]
        )
        fnc_str = fnc.__name__ + "(" + arg_str + ")"
        print(f"TOTAL TIME: {end - start}")
        return result

    return wrapper


def get_predata(queryString):
    gn = GoogleNews()
    s = gn.search(f"{queryString}", when="24h")
    preprocessed_data = []

    for entry in s["entries"]:
        item = {
            "title": entry["title"],
            "link": entry["link"],
            "published": entry["published"],
            "source": entry["source"],
        }
        if detect(item["title"]) == "en":
            preprocessed_data.append(item)

    return preprocessed_data


# New updated links and title sped up
@timed
def get_data(queryString):
    preprocessed_data = get_predata(queryString)
    return main(preprocessed_data)



