import os
import json
import random
from slugify import slugify

from .. config import Config

## Functions

def load_char_data(path):
  characters = []
  for filename in os.listdir(path):
    d = load_json(path + '/' + filename)
    characters.append(d)

  return characters

### Load JSON file data
def load_json(file):
  f = open(file)
  l = json.load(f)
  return l

### Make CharID
def make_char_slug(string):
  s = slugify(string, lowercase=True, max_length=8, separator='_') + str(random.randint(1000, 9999))
  return s

def make_char_id(string):
  s = string[:12].upper().encode("utf-8").hex()
  s = s.rjust(24, '0')
  return s

### Make slug
def make_slug(string):
  s = slugify(string, lowercase=False, max_length=64, separator='_', word_boundary=True)
  return s

### Export Character
def export_char(char):
  export_path = os.path.join(Config.CHARACTERS, Config.ENGINE)
  if not os.path.exists(export_path):
    os.makedirs(export_path)

  ## call .__dict__ member of instance
  data = char.__dict__
  filename = make_slug(char.name) + '.json'
  filepath = os.path.join(export_path, filename)

  with open(filepath, "w") as outfile:
    json.dump(data, outfile, indent=2)

### Convert hex id to human-readable string id
def id2str(hex):
  s = bytes.fromhex(hex).decode("utf-8")
  return s

### Convert 8-character string to hex id
def str2id(string):
  s = string[:8].upper().encode("utf-8").hex()
  s = s.rjust(16, '0')
  return s


