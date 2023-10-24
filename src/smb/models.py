import datetime
import os
import random
import sys
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

import lib.utils as utils

from . rules import ability_level

# GLOBALS
default_stock = 3

# CLASSES
''' Mech Class '''
class MechClass(models.Model):
  objid = models.CharField(max_length=12, unique=True)
  name = models.CharField(max_length=255, unique=True)

  ''' Stats '''
  base_strength = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  base_defense = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  base_dexterity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  base_hull = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  base_repair_kits = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  base_shields = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  base_skill_points = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
  description = models.TextField(blank=True, null=True)

  ''' DB Info '''
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  date_modified = models.DateTimeField('Date Modified', auto_now_add=True)

  ''' Meta '''
  class Meta:
    ordering = ["name"]
    verbose_name = "Mech Class"
    verbose_name_plural = "Mech Classes"

  def __str__(self):
    return self.name

''' Character '''
class Mech(models.Model):
  ''' Character Info '''
  mech_id = models.IntegerField(default=utils.gen_charid(),
    unique=True, editable=False)
  name = models.CharField(max_length=255, unique=True)
  rank = models.IntegerField(default=1,
    validators=[MinValueValidator(1), MaxValueValidator(99)])
  mech_class = models.ForeignKey('MechClass', blank=True, null=True,
    on_delete=models.SET_NULL)

  ''' Mech Build '''
  strength = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  defense = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  dexterity = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  hull = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  repair_kits = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  shields = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])
  skill_points = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(99)])

  ''' Inventory '''

  credits = models.IntegerField(default=0, 
    validators=[MinValueValidator(0), MaxValueValidator(999999)])

  ''' Profile '''
  bio = models.TextField(blank=True, null=True)
  avatar = models.ImageField(upload_to='smb/avatars',
    blank=True, null=True)

  ''' DB Info '''
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  date_modified = models.DateTimeField('Date Modified', auto_now=True)

  hull_points = 100


  ''' Mech Stats '''
  def get_stat_total(self, stat, base_stat):
    stat = stat + base_stat
    return stat

  def total_strength(self):
    return self.get_stat_total(self.strength, self.mech_class.base_strength)

  def total_defense(self):
    return self.get_stat_total(self.defense, self.mech_class.base_defense)

  def total_dexterity(self):
    return self.get_stat_total(self.dexterity, self.mech_class.base_dexterity)

  def total_hull(self):
    return self.get_stat_total(self.hull, self.mech_class.base_hull)

  def stock_repair_kits(self):
    total = self.get_stat_total(self.repair_kits, self.mech_class.base_repair_kits)
    total = total + default_stock
    return total

  def stock_shields(self):
    total = self.get_stat_total(self.shields, self.mech_class.base_shields)
    total = total + default_stock
    return total

  def stock_skill_points(self):
    total = self.get_stat_total(self.skill_points, self.mech_class.base_skill_points)
    total = total + default_stock
    return total

  '''Hit Die'''
  def get_hit_die(self, score):
    for a in ability_level:
      if score in a['score']:
        hit_die = a['die']
      elif score > 10:
        hit_die = '1d20'
      elif score < 0:
        hit_die = '1d4'
    return hit_die

  def strength_hit_die(self):
    return self.get_hit_die(self.total_strength())

  def defense_hit_die(self):
    return self.get_hit_die(self.total_defense())

  def dexterity_hit_die(self):
    return self.get_hit_die(self.total_dexterity())

  def hull_range(self):
    int_range = utils.get_range(self.total_hull())
    return int_range

  def repair_kit_range(self):
    int_range = utils.get_range(self.stock_repair_kits())
    return int_range

  def shields_range(self):
    int_range = utils.get_range(self.stock_shields())
    return int_range

  def skill_points_range(self):
    int_range = utils.get_range(self.stock_skill_points())
    return int_range

  def max_hit_points(self):
    return 1000 + (self.total_hull() * 50)

  ''' Meta '''
  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name

''' Match '''
class Match(models.Model):
  name = models.CharField(max_length=255, unique=True)
  mechs = models.ManyToManyField(Mech)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  date_modified = models.DateTimeField('Date Modified', auto_now_add=True)

  ''' Meta '''
  class Meta:
    ordering = ["date_modified"]
    verbose_name_plural = "Matches"

  def __str__(self):
    return self.name
