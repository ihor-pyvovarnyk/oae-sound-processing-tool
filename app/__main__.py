import sys

from app import Application
import config

if __name__ == '__main__':
    app = Application(config)
    app.run()
