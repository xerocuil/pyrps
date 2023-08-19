import os
import json
import random
from slugify import slugify

# Functions

## Decode base64 img
def decode_b64img(img, filename):
  with open(filename, "wb") as f:
    f.write(base64.b64decode(img))

## Load JSON characters from directory
def load_char_data(path):
  characters = []
  for filename in os.listdir(path):
    print(filename)
    d = load_json(path + '/' + filename)
    characters.append(d)
  return characters

## Load JSON file
def load_json(file):
  f = open(file)
  l = json.load(f)
  return l

## Generate Character ID (SLUG)
def make_char_slug(string):
  s = slugify(string, lowercase=True, max_length=8, separator='_') + str(random.randint(1000, 9999))
  return s

## Generate Character ID (HEX)
def make_char_id(string):
  s = string[:12].upper().encode("utf-8").hex()
  s = s.rjust(24, '0')
  return s

### Generate slug from string
def make_slug(string):
  s = slugify(string, lowercase=False, max_length=64, separator='_', word_boundary=True)
  return s

### Export Character to JSON file
def export_char(char, path):
  if not os.path.exists(path):
    os.makedirs(path)

  ## call .__dict__ member of instance
  data = char.__dict__
  filename = make_slug(char.name) + '.json'
  filepath = os.path.join(path, filename)

  with open(filepath, "w") as outfile:
    json.dump(data, outfile, indent=2)

### Convert hex ID to human-readable string ID
def id2str(hex):
  s = bytes.fromhex(hex).decode("utf-8")
  return s

### Convert 8-character max string to hex ID
def str2id(string):
  s = string[:8].upper().encode("utf-8").hex()
  s = s.rjust(16, '0')
  return s
