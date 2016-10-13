"""Cloud Foundry test"""
from flask import Flask
import os
from ctypes import *

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
	# return 'Hello world'
    try:
      leptonica = cdll.LoadLibrary(".heroku/vendor/lib/liblept.so.4.0.2")
      return 'Hello World! loaded liblept'
    except (OSError):
      logger.info("ERROR LOADING leptlib: ")
      return 'Hello World! could not load liblept'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)