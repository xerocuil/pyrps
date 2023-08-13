import os
import base64
import json
# import lib.stats as stats

# from configparser import ConfigParser
# from slugify import slugify
from flask import Flask
from flask import render_template
from flask_table import *

from lib.config import Config
# import lib.utils as Utils
import engine.dnd as Engine

# char_path = os.path.join(Config.CHARACTERS, Config.ENGINE)
# players = Utils.load_char_data(char_path)

players = [{"name": "Huey", "level": 2, "char_class": "Ranger", "id": 209394}, {"name": "Dewey", "level": 2, "char_class": "Fighter", "id": 209395}, {"name": "Louie", "level": 3, "char_class": "Mage", "id": 209393}]

# ## Init Players
# Player1 = []
# Player2 = []

# Player1 = [Engine.Char1, Engine.Char3]
# Player2 = [Engine.Char2]

# players = [Player1, Player2]

# Utils.export_char(Engine.Char1)
# Utils.export_char(Engine.Char2)
# Utils.export_char(Engine.Char3)


## Init Flask App
app = Flask(__name__)


## Routes

### Home

@app.route('/')
@app.route('/index')
def index():
  return  render_template('dnd/characters.html', players=Engine.players, char_default=Engine.char_default)

### Characters

@app.route('/characters')
def characters():
  return  render_template('dnd/characters.html', players=Engine.players, char_default=Engine.char_default)

### Char. classes
@app.route('/classes')
def charClasses():
  return  render_template('dnd/classes.html', char_class=Engine.char_class)

### Char. sheet
@app.route('/csheet/<char_id>', methods=['GET', 'POST'])
def charSheet(char_id):
  character = {}
  for c in Engine.players:
    if c['id'] == char_id:
      character = c
      print(type(character))
  return  render_template('dnd/csheet.html', character=character)


## Run App
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8088, debug=True)

