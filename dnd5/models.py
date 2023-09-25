import datetime
import os
import random
import sys
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from . rules import Arcane, Combat, Equipment, General


# FUNCTIONS
def gen_charid():
  int = random.randint(100000, 999999)
  return int


# TEXT CHOICES

class abilities(models.TextChoices):
  STR = 'STR', _('Strength: Natural athleticism, bodily power')
  DEX = 'DEX', _('Dexterity: Physical agility, reflexes, balance, poise')
  CON = 'CON', _('Constitution: Health, stamina, vital force')
  INT = 'INT', _('Intelligence: Mental acuity, information recall, analytical skill')
  WIS = 'WIS', _('Wisdom: Awareness, intuition, insight')
  CHA = 'CHA', _('Charisma: Confidence, eloquence, leadership')

class damageType(models.TextChoices):
  ACID = 'ACID', _('Acid')
  BLUDGEON = 'BLUDGEON', _('Bludgeoning')
  COLD = 'COLD', _('Cold')
  FIRE = 'FIRE', _('Fire')
  FORCE = 'FORCE', _('Force')
  LIGHTNING = 'LIGHTNING', _('Lightning')
  NECROTIC = 'NECROTIC', _('Necrotic')
  PIERCING = 'PIERCING', _('Piercing')
  POISON = 'POISON', _('Poison')
  PSYCHIC = 'PSYCHIC', _('Psychic')
  RADIANT = 'RADIANT', _('Radiant')
  SLASHING = 'SLASHING', _('Slashing')
  THUNDER = 'THUNDER', _('Thunder')

class sources(models.TextChoices):
  SRD = 'SRD', _('System Reference Document')
  OGC = 'OGC', _('Open Game Content')
  HB = 'HB', _('Homebrew')


# EQUIPMENT

## Categories
class equipmentCategory(models.TextChoices):
  AMMO = 'AMMO', _('Ammunition')
  ARMORHVY = 'ARMORHVY', _('Heavy Armor')
  ARMORLT = 'ARMORLT', _('Light Armor')
  ARMORMD = 'ARMORMD', _('Medium Armor')
  FIREARM = 'FIREARM', _('Firearm')
  POTION = 'POTION', _('Potion')
  SHIELD = 'SHIELD', _('Shield')
  WEAPONMARTL = 'WEAPONMARTL', _('Martial Weapon')
  WEAPONSIMPLE = 'WEAPONSIMPLE', _('Simple Weapon')

## Armor
class Armor(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  category = models.CharField(max_length=12, choices=equipmentCategory.choices)
  armor_class = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  strength = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  stealth_disadvantage = models.BooleanField(default=False, blank=True, null=True)
  modifier = models.CharField(max_length=12, choices=abilities.choices, blank=True, null=True)
  modifier_max = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  damage = models.CharField(max_length=6, blank=True, null=True)
  damage_type = models.CharField(max_length=12, choices=damageType.choices, blank=True, null=True)
  stat_mod = models.CharField(max_length=96, blank=True, null=True)
  properties = models.CharField(max_length=255, blank=True, null=True)
  cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
    verbose_name = "Armor"
    verbose_name_plural = "Armor"

## Shield
class Shield(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  category = models.CharField(max_length=12, choices=equipmentCategory.choices)
  armor_class = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  strength = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  stealth_disadvantage = models.BooleanField(default=False, blank=True, null=True)
  modifier = models.CharField(max_length=12, choices=abilities.choices, blank=True, null=True)
  modifier_max = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  damage = models.CharField(max_length=6, blank=True, null=True)
  damage_type = models.CharField(max_length=12, choices=damageType.choices, blank=True, null=True)
  stat_mod = models.CharField(max_length=96, blank=True, null=True)
  properties = models.CharField(max_length=255, blank=True, null=True)
  cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]

## Weapon
class Weapon(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  category = models.CharField(max_length=12, choices=equipmentCategory.choices)
  ### Combat Stats
  damage = models.CharField(max_length=64, blank=True, null=True)
  damage_type = models.CharField(max_length=12, choices=damageType.choices)
  ranges = models.CharField(max_length=255, blank=True, null=True)
  properties = models.CharField(max_length=255, blank=True, null=True)
  versatile_damage = models.CharField(max_length=6, blank=True, null=True)
  ### Weapon Info
  cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
  weight = models.DecimalField(max_digits=6, decimal_places=2, default=0)
  description = models.TextField(blank=True, null=True)
  ### DB Info
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]


# ARCANE

## Spell
class Spell(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  level = models.IntegerField(default=0,
    validators=[MinValueValidator(0), MaxValueValidator(9)])
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  # CONT


# COMBAT

## Challenge Ratings
class ChallengeRatings(models.TextChoices):
  CR0 = 'CR0', _('CR: 0')
  CR1_8 = 'CR1/8', _('CR: 1/8')
  CR1_4 = 'CR1/4', _('CR: 1/4')
  CR1_2 = 'CR1/2', _('CR: 1/2')
  CR1 = 'CR1', _('CR: 1')
  CR2 = 'CR2', _('CR: 2')
  CR3 = 'CR3', _('CR: 3')
  CR4 = 'CR4', _('CR: 4')
  CR5 = 'CR5', _('CR: 5')
  CR6 = 'CR6', _('CR: 6')
  CR7 = 'CR7', _('CR: 7')
  CR8 = 'CR8', _('CR: 8')
  CR9 = 'CR9', _('CR: 9')
  CR10 = 'CR10', _('CR: 10')
  CR11 = 'CR11', _('CR: 11')
  CR12 = 'CR12', _('CR: 12')
  CR13 = 'CR13', _('CR: 13')
  CR14 = 'CR14', _('CR: 14')
  CR15 = 'CR15', _('CR: 15')
  CR16 = 'CR16', _('CR: 16')
  CR17 = 'CR17', _('CR: 17')
  CR18 = 'CR18', _('CR: 18')
  CR19 = 'CR19', _('CR: 19')
  CR20 = 'CR20', _('CR: 20')
  CR21 = 'CR21', _('CR: 21')
  CR22 = 'CR22', _('CR: 22')
  CR23 = 'CR23', _('CR: 23')
  CR24 = 'CR24', _('CR: 24')
  CR25 = 'CR25', _('CR: 25')
  CR26 = 'CR26', _('CR: 26')
  CR27 = 'CR27', _('CR: 27')
  CR28 = 'CR28', _('CR: 28')
  CR29 = 'CR29', _('CR: 29')
  CR30 = 'CR30', _('CR: 30')

## Monster Types
class MonsterTypes(models.TextChoices):
  ABERRATION = 'ABERRATION', _('Aberration')
  BEAST = 'BEAST', ('Beast')
  CELESTIAL = 'CELESTIAL', ('Celestial')
  CONSTRUCT = 'CONSTRUCT', ('Construct')
  DRAGON = 'DRAGON', ('Dragon')
  ELEMENTAL = 'ELEMENTAL', ('Elemental')
  FEY = 'FEY', ('Fey')
  FIEND = 'FIEND', ('Fiend')
  GIANT = 'GIANT', ('Giant')
  HUMANOID = 'HUMANOID', ('Humanoid')
  MONSTROSITY = 'MONSTROSITY', ('Monstrosity')
  OOZE = 'OOZE', ('Ooze')
  PLANT = 'PLANT', ('Plant')
  UNDEAD = 'UNDEAD', ('Undead')

## Monsters
class Monster(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  challenge_rating = models.CharField(max_length=255,
    choices=ChallengeRatings.choices, 
    blank=True, null=True)
  monster_type = models.CharField(max_length=12, choices=MonsterTypes.choices,
    blank=True, null=True)
  ### Abilities
  strength = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  dexterity = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  constitution = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  intelligence = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  wisdom = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  charisma = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  ### Combat Stats
  hit_points = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(999999)])
  speed = models.IntegerField(default=25,
    validators=[MinValueValidator(1), MaxValueValidator(999)])
  actions = models.CharField(max_length=255, blank=True, null=True)
  damage_immunities = models.CharField(max_length=255, blank=True, null=True)
  condition_immunities = models.CharField(max_length=255, blank=True, null=True)
  ### Monster Profile
  language = models.CharField(max_length=255, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  ### DB Info
  source = models.CharField(max_length=12, choices=sources.choices,
    blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)


# CHARACTERS

## Character Class
class Cclass(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  hit_die = models.IntegerField(default=8,
    validators=[MinValueValidator(4), MaxValueValidator(20)])
  primary = models.CharField(max_length=255, blank=True, null=True)
  stp = models.CharField('Saving Throw Prof.',
    max_length=255, blank=True, null=True)
  awp = models.CharField('Armor/Weapon Prof.',
    max_length=255, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices,
    blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
    verbose_name = "Class"
    verbose_name_plural = "Classes"

## Race
class Race(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)
  ability_score = models.CharField(max_length=96, blank=True, null=True)
  # speed = models.CharField('Speed (ft.)', max_length=16, blank=True, null=True)
  speed = models.IntegerField(
    validators=[MinValueValidator(0),MaxValueValidator(500)], default=25)
  language = models.CharField(max_length=255, blank=True, null=True)
  addl_language = models.IntegerField(
    validators=[MinValueValidator(1),MaxValueValidator(99)],
    blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices,
    blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
    verbose_name = "Race"
    verbose_name_plural = "Race"

## Character
class Character(models.Model):
  ## Character Info
  charid = models.IntegerField(default=gen_charid,
    unique=True, editable=False)
  name = models.CharField(max_length=255, unique=True)
  level = models.IntegerField(default=1,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  cclass = models.ForeignKey('Cclass', blank=True, null=True,
    on_delete=models.SET_NULL)
  ### Abilities
  strength = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  dexterity = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  constitution = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  intelligence = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  wisdom = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  charisma = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  ### Misc Stats
  inspiration = models.IntegerField(default=0,
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  ### Equipment
  weapon_main = models.ForeignKey(Weapon,
    on_delete=models.SET_NULL,
    blank=True, null=True,
    related_name='weapon_main')
  weapon_secondary = models.ForeignKey(Weapon,
    on_delete=models.SET_NULL,
    blank=True, null=True,
    related_name='weapon_secondary')
  armor = models.ForeignKey(Armor,
    on_delete=models.SET_NULL,
    blank=True, null=True,
    related_name='armor')
  shield = models.ForeignKey(Shield,
    on_delete=models.SET_NULL,
    blank=True, null=True)
  ### Character Profile
  race = models.ForeignKey(Race, on_delete=models.SET_NULL,
    blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  avatar = models.ImageField(upload_to='dnd5/avatars',
    blank=True, null=True)

  ### DB Info
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  date_modified = models.DateTimeField('Date Modified', auto_now=True)

  def __str__(self):
    return self.name

  ### Prof. Bonus
  def get_proficiency_bonus(self, level):
    for c in General.CharacterAdvancement.LIST:
      if level == c['level']:
        return c['proficiency_bonus']

  def proficiency_bonus(self):
    return self.get_proficiency_bonus(self.level)

  ### Ability Modifiers
  def ability_mod(self, score):
    for a in General.AbilityModifier.LIST:
      if score in a['score']:
        return a['modifier']

  def strength_mod(self):
    return self.ability_mod(self.strength)

  def dexterity_mod(self):
    return self.ability_mod(self.dexterity)

  def constitution_mod(self):
    return self.ability_mod(self.constitution)

  def intelligence_mod(self):
    return self.ability_mod(self.intelligence)

  def wisdom_mod(self):
    return self.ability_mod(self.wisdom)

  def charisma_mod(self):
    return self.ability_mod(self.charisma)

  ### Hit Points
  def hit_points(self):
    hp = self.level * (self.constitution_mod() + (self.cclass.hit_die/2) + 1)
    return int(hp)

  ### Meta
  class Meta:
    ordering = ["name"]



