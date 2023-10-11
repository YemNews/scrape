import requests
import time
from gnews import get_data

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.2f} seconds to execute")
        return result
    return wrapper

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

def quick_load(link):
    try:
        response = requests.head(link, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            final_url = response.url
            print(f'Final URL: {final_url}\n')
        else:
            print("Failed to retrieve the final URL. Status code:", response.status_code)
    except:
        print("\nTIMEOUT")
   
def load(link):
    try:
        response = requests.get(link, timeout=5)
        if response.status_code == 200:
            final_url = response.url
            print(f'Final URL: {final_url}\n')
        else:
            print("Failed to retrieve the final URL. Status code:", response.status_code)
    except:
        print('TIMEOUT')

data = get_data("Generative AI","general")
middle_links = [item['link'] for item in data]

@timed
def get_endpoints(middle_links, function):
    for link in middle_links:
        function(link)

print('BEFORE OPTIMIZATION:', get_endpoints(middle_links, load))
print('AFTER OPTIMIZATION 🔥🔥🔥: ', get_endpoints(middle_links, quick_load))
print(len(middle_links))


