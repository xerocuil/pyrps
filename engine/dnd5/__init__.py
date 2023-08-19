import os
import base64
import json
import random
import sys

sys.path.append('../../lib')

from lib import config as Config

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

## Convert JSON data to object
for cc in char_class:
  globals()[cc['slug']] = charClassDec(cc)

for ch in char_data:
  globals()[ch['slug']] = jsonDec('Character', ch)
  CHARACTERS.append(globals()[ch['slug']])


