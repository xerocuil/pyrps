import datetime
import random
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def gen_char_id():
  int = random.randint(100000, 999999)
  return int

class Cclass(models.Model):
  name = models.CharField(max_length=128, unique=True)
  description = models.TextField(blank=True, null=True)
  hit_die = models.IntegerField(default=8, validators=[MinValueValidator(4), MaxValueValidator(20)])
  primary = models.CharField(max_length=128, blank=True, null=True)
  stp = models.CharField(max_length=128, blank=True, null=True)
  awp = models.CharField(max_length=128, blank=True, null=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
    verbose_name = "Class"
    verbose_name_plural = "Classes"

class Character(models.Model):
  char_id = models.IntegerField(default=gen_char_id, unique=True, editable=False)
  name = models.CharField(max_length=128, unique=True)
  level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
  cclass = models.ForeignKey('Cclass', blank=True, null=True, on_delete=models.CASCADE)
  bio = models.TextField(blank=True, null=True)

  ## STATS
  strength = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
  dexterity = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
  constitution = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
  intelligence = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
  wisdom = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
  charisma = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])

  # profile_pic = models.TextField(blank=True, null=True)
  avatar = models.ImageField(blank=True, null=True, upload_to='dnd5/avatars')

  ## DB INFO
  date_added = models.DateTimeField('Date Added', auto_now_add=True)
  date_modified = models.DateTimeField('Date Modified', auto_now=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]


  
