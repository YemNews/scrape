import requests
import concurrent.futures
from gnews import get_data

def timed(fnc):
    from functools import wraps
    import time
    @wraps(fnc)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fnc(*args, **kwargs)
        end = time.time()
        arg_str = ','.join([str(arg) for arg in args] + \
                  ['{0}={1}'.format(k, v) for (k, v) in kwargs])
        fnc_str = fnc.__name__ + '(' + arg_str + ')'
        print(f'TOTAL TIME: {end - start}')
        return result
    return wrapper

def fetch_redirect_url(link):
    try:
        response = requests.get(link, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            final_url = response.url
            return final_url
        else:
            return f"Failed to retrieve the final URL. Status code: {response.status_code}"
    except Exception as e:
        return f"Failed to retrieve the final URL: {str(e)}"

def load(link):
    try:
        response = requests.get(link, timeout=5)
        if response.status_code == 200:
            final_url = response.url
            # print(f'Final URL: {final_url}\n')
        else:
            print("Failed to retrieve the final URL. Status code:", response.status_code)
    except:
        print('TIMEOUT')

@timed
def main():
    data = get_data("Generative AI","general")
    middle_links = [item['link'] for item in data]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(fetch_redirect_url, middle_links))

    for link, final_url in zip(middle_links, results):
        # print(f"Original URL: {link}")
        print(f"Final URL: {final_url}\n")

@timed
def normal():
    data = get_data("Generative AI","general")
    middle_links = [item['link'] for item in data]
    for link in middle_links:
        load(link)

if __name__ == "__main__":
    main()
    normal()

