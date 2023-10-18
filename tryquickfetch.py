import requests
import concurrent.futures
from bs4 import BeautifulSoup as bs

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

def fetch_redirect_url(preprocessed_data):
    try:
        processed_data = preprocessed_data
        response = requests.get(preprocessed_data['link'], allow_redirects=True, timeout=5)
        if response.status_code == 200:
            final_url = response.url
            soup = bs(response.text, 'html.parser')
            title = soup.find('title').text
            
            processed_data['endlink'] = final_url
            processed_data['endtitle'] = title

            return processed_data
    except Exception as e:
        return f"Failed to retrieve the final URL: {str(e)}"



def main(preprocessed_data):
    data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(fetch_redirect_url, preprocessed_data))
    
    for item in results:
        if isinstance(item, dict):
            data.append(item)

    return data


