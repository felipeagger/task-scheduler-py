import requests
import random
import time

from huey import crontab

from src.app import huey
from src.settings import URL


@huey.task()
def get_request(url, origin: str):

    try:
        req = requests.get(url)
        body = req.json() if req.ok else req.text

        print(f'get_request - origin: {origin} -> status_code: {req.status_code}')
        time.sleep(random.randint(0, 3))

        return req.status_code, body

    except Exception as e:
        print(f'Error get_request - origin: {origin} -> {str(e)}')
        return str(e), 500


@huey.task(retries=2, retry_delay=5)
def get_request_with_retry(url: str):

    req = requests.get(url)

    if random.randint(0, 1) == 0:
        print(f'get_request_with_retry failed')
        raise Exception('failing to test retry!')

    print(f'get_request_with_retry -> status_code: {req.status_code}')
    return req.status_code, req.json() if req.ok else req.text


@huey.periodic_task(crontab(minute='*/1'))
def periodic_request():
    print('periodic execution')
    new_task = get_request(URL, 'cron')
    status, _ = new_task(blocking=True)
