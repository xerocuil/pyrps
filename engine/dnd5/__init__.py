import os
import base64
import json
import random
import sys

from flask import Blueprint, render_template, request, url_for, flash, redirect

# sys.path.append('../../lib')

# from lib import config as Config

from collections import namedtuple
from json import JSONEncoder
from slugify import slugify


# Global Variables

ENG_DIR = os.path.dirname(os.path.realpath(__file__))
ENG_DATA = os.path.join(ENG_DIR, 'data')
ENG_NAME = 'D&D: 5th Edition'
ENG_SLUG = 'dnd5'

CHARACTERS = []

# Functions

## Decode JSON dict to object
def charClassDec(cDict):
    return namedtuple('Class', cDict.keys())(*cDict.values())

def jsonDec(name, jdict):
    return namedtuple(name, jdict.keys())(*jdict.values())

## Load JSON file
def load_json(file):
  f = open(file)
  l = json.load(f)
  return l

## Generate Character ID (HEX)
def make_char_id(string):
  s = string[:12].upper().encode("utf-8").hex()
  s = s.rjust(24, '0')
  return s

## Generate Character ID (SLUG)
def make_char_slug(string):
  s = slugify(string, lowercase=True, max_length=12, separator='') + str(random.randint(1000, 9999))
  s = s.upper()
  return s

# #### Query char_class
# def query_char_class(id_str):
#   class_id = str2id(id_str)
#   for q in char_class:
#     if q['id'] == class_id:
#       return q

### Convert hex ID to human-readable string ID
def id2str(hex):
  s = bytes.fromhex(hex).decode("utf-8")
  return s

### Convert 8-character max string to hex ID
def str2id(string):
  s = string[:16].upper().encode("utf-8").hex()
  s = s.rjust(32, '0')
  return s


# Init Char. Classes

## Load JSON data
char_data = load_json(ENG_DATA + '/characters.json')
char_class = load_json(ENG_DATA + '/char_class.json')

# print('ENG_DATA: ' + str(ENG_DATA))

## Convert JSON data to object
for cc in char_class:
  globals()[cc['slug']] = charClassDec(cc)

for ch in char_data:
  globals()[ch['slug']] = jsonDec('Character', ch)
  CHARACTERS.append(globals()[ch['slug']])


dnd5 = Blueprint('dnd5', __name__,
  template_folder='templates',
  static_folder='static',
  static_url_path='assets')


@dnd5.route('/')
def index():
  return render_template('dnd5/index.html', characters=CHARACTERS)


## DND: Add char
@dnd5.route('/addChar', methods=('GET', 'POST'))
def addChar():
  if request.method == 'POST':
    name = request.form['name']
    level = request.form['level']
    char_class = request.form['char_class']
    strength = request.form['strength']
    dexterity = request.form['dexterity']
    constitution = request.form['constitution']
    
    csheet = []
    csheet_data = {
      "name": name,
      "level": level,
      "char_class": char_class,
      "strength": strength,
      "dexterity": dexterity,
      "constitution": constitution,
    }
    
    csheet = [csheet_data]
    print(csheet)

    if not name:
      flash('Name is required!')
    elif not level:
      flash('Level is required!')
    else:
      csheet.append(csheet_data)

      char_file = os.path.join(ENG_DATA, 'characters.json')
      if not os.path.exists(char_file):
        os.makedirs(char_dir)
        with open(char_file, "w") as outfile:
          json.dump(csheet, outfile, indent=2)
      else:
        characters = load_json(char_file)
        characters.append(csheet_data)
        with open(char_file, 'w') as outfile:
          json.dump(characters, outfile, indent=2)


      return redirect(url_for('dnd5.index'))

  return render_template('dnd5/addChar.html', characters=CHARACTERS)




@dnd5.route('/editChar')
def editChar():
  return render_template('dnd5/editChar.html', characters=CHARACTERS)