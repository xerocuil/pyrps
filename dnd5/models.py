import datetime
import random
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


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

class sources(models.TextChoices):
  SRD = 'SRD', _('5th Edition System Reference Document')
  HB = 'HB', _('Homebrew')
  OGC = 'OGC', _('Open Game Content')

# CLASSES
class Armor(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=128, unique=True)
  category = models.CharField(max_length=12, choices=equipmentCategory.choices)
  armor_class = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  strength = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
  stealth_disadvantage = models.BooleanField(default=False, blank=True, null=True)
  modifier = models.CharField(max_length=12, choices=abilities.choices, blank=True, null=True)
  modifier_max = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
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


class Cclass(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=128, unique=True)
  hit_die = models.IntegerField(default=8, validators=[MinValueValidator(4), MaxValueValidator(20)])
  primary = models.CharField(max_length=128, blank=True, null=True)
  stp = models.CharField('Saving Throw Prof.', max_length=128, blank=True, null=True)
  awp = models.CharField('Armor/Weapon Prof.', max_length=128, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
    verbose_name = "Class"
    verbose_name_plural = "Classes"


class Spell(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=128, unique=True)
  level = models.IntegerField(default=0,
    validators=[MinValueValidator(0), MaxValueValidator(9)])
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  # CONT


class Weapon(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=128, unique=True)
  category = models.CharField(max_length=12, choices=equipmentCategory.choices)
  damage = models.CharField(max_length=6)
  damage_type = models.CharField(max_length=12, choices=damageType.choices)
  cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
  weight = models.DecimalField(max_digits=6, decimal_places=2, default=0)
  wp_range = models.CharField(max_length=128, blank=True, null=True)
  wp_properties = models.CharField(max_length=128, blank=True, null=True)
  v_damage = models.CharField(max_length=6, blank=True, null=True)
  source = models.CharField(max_length=64, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  source = models.CharField(max_length=12, choices=sources.choices, blank=True, null=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]


class Character(models.Model):
  ## CHARACTER INFO
  charid = models.IntegerField(default=gen_charid,
    unique=True, editable=False)
  name = models.CharField(max_length=128, unique=True)
  level = models.IntegerField(default=1,
    validators=[MinValueValidator(1), MaxValueValidator(20)])
  cclass = models.ForeignKey('Cclass', blank=True, null=True,
    on_delete=models.SET_NULL)

  ## STATS
  strength = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(20)])
  dexterity = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(20)])
  constitution = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(20)])
  intelligence = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(20)])
  wisdom = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(20)])
  charisma = models.IntegerField(default=10,
    validators=[MinValueValidator(1), MaxValueValidator(20)])

  ## EQUIPMENT
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
    blank=True, null=True)

  ## CHARACTER PROFILE
  avatar = models.ImageField(blank=True, null=True, upload_to='dnd5/avatars')
  bio = models.TextField(blank=True, null=True)

  ## DB INFO
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  date_modified = models.DateTimeField('Date Modified', auto_now=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
