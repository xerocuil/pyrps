import base64
import datetime
import json
import os
import random
import sqlite3
from slugify import slugify

# GLOBALS
APPDIR = os.path.dirname(os.path.realpath(__file__))
MEDIA = os.path.join(APPDIR, 'media')
DND5_AVATARS = os.path.join(MEDIA, 'dnd5/avatars')


# DATABASE

## Connect
connection = sqlite3.connect('db.sqlite3')
## Create cursor object
cursor = connection.cursor()


# FUNCTIONS




##### REVIEW #####

# ### Import characters from csv file
# def import_characters():
#   file = pd.read_csv('dnd5/data/characters.csv', sep=';')
#   data = file.to_dict(orient='records')
#   for d in data:
#     ## Get cclass ID
#     class_query = "SELECT * from dnd5_cclass WHERE objid = '" + d['cclass'] +"';"
#     try:
#       class_result = cursor.execute(class_query)
#       class_r = cursor.fetchall()
#     except Exception as e:
#       # print(e)
#       class_result = e
#       print(class_result)

#     ## Get Race ID
#     if isinstance(d['race'], str):
#       # print("d['race']:")
#       # print(d['race'])

#       race_query = "SELECT id from dnd5_race WHERE objid = '" + d['race'] +"';"
#       try:
#         race_result = cursor.execute(race_query)
#         race_r = cursor.fetchone()
#         race_id = race_r[0]
#       except Exception as e:
#         race_result = e
#         print(race_result)
#         race_id = None
#     else:
#       # print(d['race'])
#       race_id = None

#     ## Get main weapon ID
#     if isinstance(d['weapon_main'], str):
#       # print("d['weapon_main']:")
#       # print(d['weapon_main'])

#       weapon_main_query = "SELECT id from dnd5_weapon WHERE objid = '" + d['weapon_main'] +"';"
#       try:
#         weapon_main_result = cursor.execute(weapon_main_query)
#         weapon_main_r = cursor.fetchone()
#         weapon_main_id = weapon_main_r[0]
#       except Exception as e:
#         weapon_main_result = e
#         # print(weapon_main_result)
#         weapon_main_id = None
#     else:
#       # print(d['weapon_main'])
#       weapon_main_id = None

#     ## Get secondary weapon ID
#     if isinstance(d['weapon_secondary'], str):
#       # print("d['weapon_secondary']:")
#       # print(d['weapon_secondary'])

#       weapon_secondary_query = "SELECT id from dnd5_weapon WHERE objid = '" + d['weapon_secondary'] +"';"
#       try:
#         weapon_secondary_result = cursor.execute(weapon_secondary_query)
#         weapon_secondary_r = cursor.fetchone()
#         weapon_secondary_id = weapon_secondary_r[0]
#       except Exception as e:
#         weapon_secondary_result = e
#         # print(weapon_secondary_result)
#         weapon_secondary_id = None
#     else:
#       # print(d['weapon_secondary'])
#       weapon_secondary_id = None

#     ## Get armor ID
#     if isinstance(d['armor'], str):
#       # print("d['armor']:")
#       # print(d['armor'])

#       armor_query = "SELECT id from dnd5_armor WHERE objid = '" + d['armor'] +"';"
#       try:
#         armor_result = cursor.execute(armor_query)
#         armor_r = cursor.fetchone()
#         armor_id = armor_r[0]
#       except Exception as e:
#         armor_result = e
#         # print(armor_result)
#         armor_id = None
#     else:
#       # print(d['armor'])
#       armor_id = None


#     ## Get shield ID
#     if isinstance(d['shield'], str):
#       # print("d['shield']:")
#       # print(d['shield'])

#       shield_query = "SELECT id from dnd5_shield WHERE objid = '" + d['shield'] +"';"
#       try:
#         shield_result = cursor.execute(shield_query)
#         shield_r = cursor.fetchone()
#         shield_id = shield_r[0]
#       except Exception as e:
#         shield_result = e
#         # print(shield_result)
#         shield_id = None
#     else:
#       # print(d['shield'])
#       shield_id = None

#     ## Get Avatar
#     if isinstance(d['avatar'], str):
#       file = os.path.join(DND5_AVATARS, str(d['charid']) + '.png')
#       decode_img(d['avatar'], file)
#       avatar = 'dnd5/avatars/' + str(d['charid']) + '.png'
#     else:
#       avatar = None

#     d['id'] = None
    
#     d['cclass_id'] = class_r[0][0]
#     d['inspiration'] = 0
#     d['race_id'] = race_id
#     d['weapon_main_id'] = weapon_main_id
#     d['weapon_secondary_id'] = weapon_secondary_id
#     d['armor_id'] = armor_id
#     d['shield_id'] = shield_id
#     d['avatar'] = avatar
#     d['date_added'] = datetime.datetime.now()
#     d['date_modified'] = datetime.datetime.now()

#     add_character = 'INSERT INTO dnd5_character VALUES(:id, \
#       :charid, \
#       :name, \
#       :level, \
#       :strength, \
#       :dexterity, \
#       :constitution, \
#       :intelligence, \
#       :wisdom, \
#       :charisma, \
#       :inspiration, \
#       :bio, \
#       :avatar, \
#       :date_added, \
#       :date_modified, \
#       :armor_id, \
#       :cclass_id, \
#       :race_id, \
#       :shield_id, \
#       :weapon_main_id, \
#       :weapon_secondary_id)'

#     try:
#       cursor.execute(add_character, d)
#       connection.commit()
#     except Exception as e:
#       print('Could not add ' + str(d['charid']) + '\nError message: ' + str(e) + '\n')

# # Import all models/character
# def import_all():
#   ## Armor
#   armor_query = 'INSERT INTO dnd5_armor VALUES(:id, \
#     :objid, \
#     :name, \
#     :category, \
#     :armor_class, \
#     :strength, \
#     :stealth_disadvantage, \
#     :modifier, \
#     :modifier_max, \
#     :damage, \
#     :damage_type, \
#     :stat_mod, \
#     :properties, \
#     :cost, \
#     :weight, \
#     :description, \
#     :source, \
#     :date_added)'
#   import_model('armor', armor_query)

#   ## Cclass
#   cclass_query = 'INSERT INTO dnd5_cclass VALUES(:id, \
#     :objid, \
#     :name, \
#     :hit_die, \
#     :primary, \
#     :stp, \
#     :awp, \
#     :description, \
#     :source, \
#     :date_added)'
#   import_model('cclass', cclass_query)

#   ## Race
#   race_query = 'INSERT INTO dnd5_race VALUES(:id, \
#     :objid, \
#     :name, \
#     :ability_score, \
#     :speed, \
#     :language, \
#     :addl_language, \
#     :description, \
#     :source, \
#     :date_added)'
#   import_model('race', race_query)

#   ## Armor
#   shield_query = 'INSERT INTO dnd5_shield VALUES(:id, \
#     :objid, \
#     :name, \
#     :category, \
#     :armor_class, \
#     :strength, \
#     :stealth_disadvantage, \
#     :modifier, \
#     :modifier_max, \
#     :damage, \
#     :damage_type, \
#     :stat_mod, \
#     :properties, \
#     :cost, \
#     :weight, \
#     :description, \
#     :source, \
#     :date_added)'
#   import_model('shield', shield_query)

#   ## Weapon
#   weapon_query = 'INSERT INTO dnd5_weapon VALUES(:id, \
#     :objid, \
#     :name, \
#     :category, \
#     :damage, \
#     :damage_type, \
#     :ranges, \
#     :properties, \
#     :versatile_damage, \
#     :cost, \
#     :weight, \
#     :description, \
#     :source, \
#     :date_added)'
#   import_model('weapon', weapon_query)

#   ## Characters
#   import_characters()
#   connection.close()








# DEPRECATED
# ## Load JSON characters from directory
# def load_char_data(path):
#   characters = []
#   for filename in os.listdir(path):
#     print(filename)
#     d = load_json(path + '/' + filename)
#     characters.append(d)
#   return characters

# ## Load JSON file
# def load_json(file):
#   f = open(file)
#   l = json.load(f)
#   return l

# ### Import model from csv file
# def import_model(classname, query):
#   file = pd.read_csv('dnd5/data/' + classname + '.csv', sep=';')
#   data = file.to_dict(orient='records')
#   for d in data:
#     d['id'] = None
#     d['date_added'] = datetime.datetime.now()
#     try:
#       cursor.execute(query, d)
#       connection.commit()
#     except Exception as e:
#       print('Could not add ' + d['objid'] + '\nError message: ' + str(e) + '\n')