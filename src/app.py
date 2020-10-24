from os import getenv

from gevent import monkey; monkey.patch_all()
from flask import Flask
from huey import RedisHuey


DEBUG = getenv('DEBUG', True)

app = Flask(__name__)
app.config.from_object(__name__)

huey = RedisHuey('task-scheduler', host=getenv('REDIS_HOST'), always_eager=DEBUG)
huey.immediate = False
