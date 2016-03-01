# import numpy
import sys

from app import Application
import config

# Check is into virtual env
if not hasattr(sys, 'real_prefix'):
    raise Exception('Need to run into virtual environment. Run source bin/activate for activate virtualenv')

if __name__ == '__main__':
    Application.run(config)
