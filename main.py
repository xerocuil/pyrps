import os
import base64
import json

from flask import Flask, render_template, request, url_for, flash, redirect
# from flask import render_template
from flask_table import *

import lib.config as cfg
import lib.utils as Utils

# import engine.dnd5 as dnd5


# Global variables
ENGINE = cfg.settings['SYSTEM']['ENGINE']
KEY = cfg.settings['SYSTEM']['KEY']
APPDIR = cfg.settings['FILES']['APPDIR']
ENGINEDIR = cfg.settings['FILES']['ENGINEDIR']

C_ENG_DIR = os.path.join(ENGINEDIR, ENGINE)
C_ENG_DATA = os.path.join(C_ENG_DIR, 'data')

CHAR_FILE = os.path.join(C_ENG_DATA, 'characters.json')









# Functions

## Load JSON data
def load_json(file):
  f = open(file)
  l = json.load(f)
  return l


# Load Characters
if os.path.exists(CHAR_FILE):
  characters = load_json(CHAR_FILE)
else:
  characters = []


# Init Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


# Context processors

@app.context_processor
def APPTITLE():
    return {'APPTITLE': cfg.settings['SYSTEM']['APPTITLE']}

@app.context_processor
def ENG_LOGO():
    return {'ENG_LOGO': '/assets/engine/' + ENGINE + '/logo.svg'}




# Routes

## Home
@app.route('/')
def index():
    return render_template(ENGINE + '/characters.html', characters=characters)



## DND5

## DND: Add char
@app.route('/dnd/add/char', methods=('GET', 'POST'))
def dnd_add_char():
  if request.method == 'POST':
    name = request.form['name']
    level = request.form['level']
    char_class = request.form['char_class']
    strength = request.form['strength']
    dexterity = request.form['dexterity']
    constitution = request.form['constitution']
    
    csheet = []
    data = {
      "name": name,
      "level": level,
      "char_class": char_class,
      "strength": strength,
      "dexterity": dexterity,
      "constitution": constitution,
    }
    
    # csheet = [data]
    # print(csheet)

    if not name:
      flash('Name is required!')
    elif not level:
      flash('Level is required!')
    else:
      csheet.append(data)

      if not os.path.exists(char_file):
        os.makedirs(char_dir)
        with open(char_file, "w") as outfile:
          json.dump(csheet, outfile, indent=2)
      else:
        # characters = load_json(char_file)
        characters.append(data)
        with open(char_file, 'w') as outfile:
          json.dump(characters, outfile, indent=2)


      return redirect(url_for('index'))

  return render_template('test2.html', characters=characters)



# ## DND: Characters
# @app.route('/dnd/characters')
# def characters():
#   return  render_template('dnd/characters.html', players=players, profileUrl=profileUrl)

# ## DND: Char. classes
# @app.route('/classes')
# def charClasses():
#   return  render_template('dnd/classes.html')

# ## DND: Char. sheet
# @app.route('/dnd/csheet/<char_id>', methods=['GET', 'POST'])
# def charSheet(char_id):
#   character = {}
#   for c in players:
#     if c['id'] == char_id:
#       character = c
#       print(type(character))
#   return  render_template('dnd/csheet.html', character=character)







# Run App
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8088, debug=True)