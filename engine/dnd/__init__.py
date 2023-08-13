import base64
import json
import os
import sys
import unittest 

# sys.path.append('../../lib')

from lib.config import Config
import lib.utils as Utils

## Load Engine Data
ENGINE_DIR = os.path.join(Config.ENGINE_DIR, Config.ENGINE)
CHAR_PATH = os.path.join(Config.CHARACTERS, Config.ENGINE)

### Load JSON data
char_adv = Utils.load_json(ENGINE_DIR + '/char_adv.json')
char_class = Utils.load_json(ENGINE_DIR + '/char_class.json')
char_default = Utils.load_json(ENGINE_DIR + '/char_default.json')

### Init Char. Classes
class CharClass(object):
  def __init__(self, class_id, name, description, hitDie, primary, stp, awp):
    self.class_id = class_id
    self.name = name
    self.description = description
    self.hitDie = hitDie
    self.primary = primary
    self.stp = stp
    self.awp = awp

#### Query char_class
def query_char_class(id_str):
  class_id = Utils.str2id(id_str)
  for q in char_class:
    if q['id'] == class_id:
      return q

#### Load Char. Classes
BRBARIAN = query_char_class('BRBARIAN')
BARD = query_char_class('BARD')
CLERIC = query_char_class('CLERIC')
FIGHTER = query_char_class('FIGHTER')
MONK = query_char_class('MONK')
PALADIN = query_char_class('PALADIN')
RANGER = query_char_class('RANGER')
ROGUE = query_char_class('ROGUE')
SORCERER = query_char_class('SORCERER')
WARLOCK = query_char_class('WARLOCK')
WIZARD = query_char_class('WIZARD')

### Init Characters
class Character(object):
  def __init__(self, name, level, char_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
    self.name = name
    self.level = level
    self.char_class = char_class
    self.strength = strength
    self.dexterity = dexterity
    self.constitution = constitution
    self.intelligence = intelligence
    self.wisdom = wisdom
    self.charisma = charisma
    self.id = Utils.make_char_id((Utils.make_char_slug(self.name)))
    self.engine = 'dnd'

    # self.defense = defense
    # self.stamina = stamina




if not os.path.exists(CHAR_PATH):
  os.makedirs(CHAR_PATH)


  ### Load Sample Characters
  players = []
  Char1 = Character('Crystal King', 14, FIGHTER, 16, 12, 10, 8, 10, 8)
  # players.append(Char1)

  Char2 = Character('Wedge', 12, RANGER, 12, 16, 10, 11, 13, 9)
  Char3 = Character('Biggs', 8, PALADIN, 14, 12, 10, 10, 12, 11)

  Utils.export_char(Char1)
  Utils.export_char(Char2)
  Utils.export_char(Char3)
  

print(os.listdir(CHAR_PATH))
players = Utils.load_char_data(CHAR_PATH)

# CHAR_PATH = os.path.join(Config.CHARACTERS, Config.ENGINE)

# players = Utils.load_char_data(CHAR_PATH)



### Init Action
class Action:
  def potion(player, mod):
    player.hit_points = player.hit_points + mod
    if player.hit_points > player.hit_points_max:
      player.hit_points = player.hit_points_max
    print(player.name, player.hit_points)

  def melee_attack(attacker, defender):
    attack_roll = input('\nEnter attack roll: ')
    defense_roll = input('\nEnter defense roll: ')
    attack_strength = (attacker.strength + int(attack_roll)) - (defender.defense + int(defense_roll))
    damage = attack_strength * 10
    print('defender.hit_points: ' + str(defender.hit_points))
    defender.hit_points  = defender.hit_points - damage
    print('defender.hit_points: ' + str(defender.hit_points))
    if attack_strength >= 1:
      print(attacker.name + ' does a melee attack on ' + defender.name + ' for ' + str(damage) + ' damage.')
    else:
      print('Missed.')

  def print_status(player):
    print('\n' +\
      player.name + '\n\
      Level   : ' + str(player.level) + '\n\
      Class   : ' + str(player.char_class) + '\n\
      HP    : ' + str(player.hit_points) + '\n\
      MP    : ' + str(player.mana_points) + '\n\
      STR   : ' + str(player.strength) + '\n\
      DEX   : ' + str(player.dexterity) + '\n\
      INT   : ' + str(player.intelligence) + '\n\
      DEF   : ' + str(player.defense) + '\n\
      ')

