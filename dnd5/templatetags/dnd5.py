import os
import sys
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from dnd5.apps import Dnd5Config

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rules import Arcane, Combat, Equipment, General

register = template.Library()

# Engine title
@register.simple_tag
def engine_title():
  return Dnd5Config.verbose_name

# Ability Modifier
@register.simple_tag
def ability_modifier(score):
  for a in General.AbilityModifier.LIST:
    if score in a['score']:
      return a['modifier']

# Split range
@register.simple_tag
def split_range(array):
  if len(array) > 1:
    x,y = array
    r = str(x) + '-' + str(y)
  else:
    r = array[0]
  return str(r)
