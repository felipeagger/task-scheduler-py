from os import getenv

from src.app import app
from src.app import huey
import src.tasks  # Import tasks so they are registered with Huey instance.
import src.endpoints  # Import views so they are registered with Flask app.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getenv('PORT', 8088))
