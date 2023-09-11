import datetime
import json
import os
import pandas as pd
import random
import sqlite3
from slugify import slugify


# Database

## Connect to database
connection = sqlite3.connect('db.sqlite3')

## Create cursor object to execute SQL queries
cursor = connection.cursor()


# Functions

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

def import_model(classname, query):
  file = pd.read_csv('dnd5/data/' + classname + '.csv', sep=';')
  data = file.to_dict(orient='records')
  for d in data:
    d['id'] = None
    d['date_added'] = datetime.datetime.now()
    try:
      cursor.execute(query, d)
      connection.commit()
    except Exception as e:
      print('Could not add ' + d['objid'] + '\nError message: ' + str(e) + '\n')


def import_characters():
  file = pd.read_csv('dnd5/data/characters.csv', sep=';')
  data = file.to_dict(orient='records')
  for d in data:
    ## Get cclass ID
    class_query = "SELECT * from dnd5_cclass WHERE objid = '" + d['cclass'] +"';"
    try:
      class_result = cursor.execute(class_query)
      class_r = cursor.fetchall()
    except Exception as e:
      # print(e)
      class_result = e
      print(class_result)

    ## Get Race ID
    if isinstance(d['race'], str):
      print("d['race']:")
      print(d['race'])

      race_query = "SELECT id from dnd5_race WHERE objid = '" + d['race'] +"';"
      try:
        race_result = cursor.execute(race_query)
        race_r = cursor.fetchone()
        race_id = race_r[0]
      except Exception as e:
        race_result = e
        print(race_result)
        race_id = None
    else:
      print(d['race'])
      race_id = None

    ## Get main weapon ID
    if isinstance(d['weapon_main'], str):
      print("d['weapon_main']:")
      print(d['weapon_main'])

      weapon_main_query = "SELECT id from dnd5_weapon WHERE objid = '" + d['weapon_main'] +"';"
      try:
        weapon_main_result = cursor.execute(weapon_main_query)
        weapon_main_r = cursor.fetchone()
        weapon_main_id = weapon_main_r[0]
      except Exception as e:
        weapon_main_result = e
        print(weapon_main_result)
        weapon_main_id = None
    else:
      print(d['weapon_main'])
      weapon_main_id = None

    ## Get secondary weapon ID
    if isinstance(d['weapon_secondary'], str):
      print("d['weapon_secondary']:")
      print(d['weapon_secondary'])

      weapon_secondary_query = "SELECT id from dnd5_weapon WHERE objid = '" + d['weapon_secondary'] +"';"
      try:
        weapon_secondary_result = cursor.execute(weapon_secondary_query)
        weapon_secondary_r = cursor.fetchone()
        weapon_secondary_id = weapon_secondary_r[0]
      except Exception as e:
        weapon_secondary_result = e
        print(weapon_secondary_result)
        weapon_secondary_id = None
    else:
      print(d['weapon_secondary'])
      weapon_secondary_id = None

    ## Get armor ID
    if isinstance(d['armor'], str):
      print("d['armor']:")
      print(d['armor'])

      armor_query = "SELECT id from dnd5_armor WHERE objid = '" + d['armor'] +"';"
      try:
        armor_result = cursor.execute(armor_query)
        armor_r = cursor.fetchone()
        armor_id = armor_r[0]
      except Exception as e:
        armor_result = e
        print(armor_result)
        armor_id = None
    else:
      print(d['armor'])
      armor_id = None

    d['id'] = None
    d['avatar'] = None
    d['date_added'] = datetime.datetime.now()
    d['date_modified'] = datetime.datetime.now()
    d['armor_id'] = None
    d['cclass_id'] = class_r[0][0]
    d['race_id'] = race_id
    d['weapon_main_id'] = weapon_main_id
    d['weapon_secondary_id'] = weapon_secondary_id
    d['armor_id'] = armor_id

    add_character = 'INSERT INTO dnd5_character VALUES(:id, \
      :charid, \
      :name, \
      :level, \
      :strength, \
      :dexterity, \
      :constitution, \
      :intelligence, \
      :wisdom, \
      :charisma, \
      :avatar, \
      :bio, \
      :date_added, \
      :date_modified, \
      :armor_id, \
      :cclass_id, \
      :race_id, \
      :weapon_main_id, \
      :weapon_secondary_id)'

    try:
      cursor.execute(add_character, d)
      connection.commit()
    except Exception as e:
      print('Could not add ' + str(d['charid']) + '\nError message: ' + str(e) + '\n')


# Import .csv files into models
def import_all():
  ## Armor
  armor_query = 'INSERT INTO dnd5_armor VALUES(:id, \
    :objid, \
    :name, \
    :category, \
    :armor_class, \
    :strength, \
    :stealth_disadvantage, \
    :modifier, \
    :modifier_max, \
    :damage, \
    :damage_type, \
    :stat_mod, \
    :properties, \
    :cost, \
    :weight, \
    :description, \
    :source, \
    :date_added)'
  import_model('armor', armor_query)

  ## Cclass
  cclass_query = 'INSERT INTO dnd5_cclass VALUES(:id, \
    :objid, \
    :name, \
    :hit_die, \
    :primary, \
    :stp, \
    :awp, \
    :description, \
    :source, \
    :date_added)'
  import_model('cclass', cclass_query)

  ## Race
  race_query = 'INSERT INTO dnd5_race VALUES(:id, \
    :objid, \
    :name, \
    :ability_score, \
    :speed, \
    :language, \
    :addl_language, \
    :description, \
    :source, \
    :date_added)'
  import_model('race', race_query)

  ## Weapon
  weapon_query = 'INSERT INTO dnd5_weapon VALUES(:id, \
    :objid, \
    :name, \
    :category, \
    :damage, \
    :damage_type, \
    :ranges, \
    :properties, \
    :versatile_damage, \
    :cost, \
    :weight, \
    :description, \
    :source, \
    :date_added)'
  import_model('weapon', weapon_query)

  ## Characters
  import_characters()
  connection.close()

# import_all()

