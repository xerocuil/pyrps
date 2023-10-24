import os
import random
import string
import base64
import datetime
import json
import sqlite3
from slugify import slugify

from configparser import ConfigParser


# GLOBALS
APPTITLE = 'PyRPS'
LIBDIR = os.path.dirname(os.path.abspath(__file__))
APPDIR = os.path.dirname(LIBDIR)
PROFILE = os.path.join(os.path.expanduser('~'),'.pyrps')
CONFIG_PATH = os.path.join(PROFILE,'config.ini')


# FUNCTIONS

## Create `char_id`
def gen_charid():
  int = random.randint(100000, 999999)
  return int

## Create `SECRET_KEY`
def gen_secretkey():
  key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(64))
  return key

### Generate slug from string
def gen_slug(string):
  s = slugify(string, lowercase=False, max_length=64, separator='_', word_boundary=True)
  return s

## Make range human-readable
def get_range(num):
  if num <= 0:
    int_range = [0]
  else:
    int_range = range(0, num, 1)
  return int_range

## Init config.ini
def init_config():
  config = ConfigParser()

  ### Create 'profiles' directory if missing
  if not os.path.exists(PROFILE):
    os.makedirs(PROFILE)

  ### Create config.ini
  config["MAIN"] = {
    "apptitle": APPTITLE,
    "appdir" : APPDIR,
    "debug": True,
    "key": gen_secretkey(),
    "profile": PROFILE,
    "db": os.path.join(PROFILE,'pyrps.db')
  }

  ### Write to config.ini
  with open(CONFIG_PATH, 'w') as conf_data:
    config.write(conf_data)




# LEGACY FUNCTIONS

### Convert hex ID to human-readable string ID
def id2str(hex):
  s = bytes.fromhex(hex).decode("utf-8")
  return s

### Convert 8-character max string to hex ID
def str2id(string):
  s = string[:8].upper().encode("utf-8").hex()
  s = s.rjust(16, '0')
  return s


### Export object to JSON file
def export_char(obj, path):
  if not os.path.exists(path):
    os.makedirs(path)

  ## call .__dict__ member of instance
  data = obj.__dict__
  filename = make_slug(obj.name) + '.json'
  filepath = os.path.join(path, filename)

  with open(filepath, "w") as outfile:
    json.dump(data, outfile, indent=2)


## Encode/Decode image to base64
def base_encode(img):
  with open(img, 'rb') as image_file:
    image_bytes = image_file.read()
    base64_img = base64.b64encode(image_bytes).decode('utf-8')
    return base64_img

def base_decode(img, filename):
  with open(filename, "wb") as f:
    f.write(base64.b64decode(img))

## Load JSON file
def load_json(file):
  f = open(file)
  l = json.load(f)
  return l

### Import model from csv file
def import_model(csv_file, query):
  file = pd.read_csv(csv_file)
  data = file.to_dict(orient='records')
  for d in data:
    d['id'] = None
    d['date'] = datetime.datetime.now()
    try:
      cursor.execute(query, d)
      connection.commit()
    except Exception as e:
      print('Could not add ' + d['objid'] + '\nError message: ' + str(e) + '\n')

## Generate Character ID (SLUG)
def make_char_slug(string):
  s = slugify(string, lowercase=True, max_length=8, separator='_') + str(random.randint(1000, 9999))
  return s

## Generate Character ID (HEX)
def make_char_id(string):
  s = string[:12].upper().encode("utf-8").hex()
  s = s.rjust(24, '0')
  return s