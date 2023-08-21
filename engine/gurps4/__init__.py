import base64
import json
import os
import sys
import unittest 

from flask import Blueprint, render_template
sys.path.append('../../lib')

from lib import config as Config
# from lib.config import Config
import lib.utils as Utils

# Functions

def decode_b64img(img, filename):
  with open(filename, "wb") as f:
    f.write(base64.b64decode(img))

gurps4 = Blueprint('gurps4', __name__,
  template_folder='templates',
  static_folder='static',
  static_url_path='assets')

@gurps4.route('/')
def index():
  return render_template('gurps4/index.html')
