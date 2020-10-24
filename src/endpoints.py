from flask import request

from src.app import app
from src.tasks import get_request, get_request_with_retry
from src.settings import URL


@app.route('/', methods=['GET'])
def health_check():
    return 'Running'


@app.route('/task', methods=['GET'])
def task():

    print('start task get_request')
    new_task = get_request(URL, 'endpoint immediate')
    status, body = new_task(blocking=True)

    return {'data': body}


@app.route('/schedule', methods=['GET'])
def schedule():

    print('schedule task get_request -> 5s')
    get_request.schedule(kwargs={'url': URL, 'origin': 'scheduled'}, delay=5)

    return 'task scheduled'


@app.route('/retry', methods=['GET'])
def retry():

    print('start task get_request_with_retry')
    try:
        new_task = get_request_with_retry(URL)
        status, body = new_task(blocking=True)
        return {'data': body}
    except:
        return 'failing to test retry!', 500
