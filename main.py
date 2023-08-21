import os
import base64
import json

from flask import Flask, render_template, request, url_for, flash, redirect

import lib.config as cfg
import lib.utils as utils

from engine.dnd5 import dnd5
from engine.gurps4 import gurps4
from engine.rpgm2k import rpgm2k


# Global variables
ENGINE = cfg.settings['SYSTEM']['ENGINE']
KEY = cfg.settings['SYSTEM']['KEY']
APPDIR = cfg.settings['FILES']['APPDIR']
ENGINEDIR = cfg.settings['FILES']['ENGINEDIR']

C_ENG_DIR = os.path.join(ENGINEDIR, ENGINE)
C_ENG_DATA = os.path.join(C_ENG_DIR, 'data')

CHAR_FILE = os.path.join(C_ENG_DATA, 'characters.json')


# Init app
app = Flask(__name__)


# Template tags
@app.context_processor
def APPTITLE():
    return {'APPTITLE': cfg.settings['SYSTEM']['APPTITLE']}

# @app.context_processor
# def ENG_LOGO():
#     return {'ENG_LOGO': '/assets/' + ENGINE + '/logo.svg'}


# Register blueprints
app.register_blueprint(dnd5, url_prefix='/dnd5')
app.register_blueprint(gurps4, url_prefix='/gurps4')
app.register_blueprint(rpgm2k, url_prefix='/rpgm2k')


# Routes
@app.route('/')
def index():
  return render_template('pyrps/index.html')


# Run App
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8088, debug=True)