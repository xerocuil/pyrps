from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

register = template.Library()

@register.simple_tag
def engine_title():
  engine_title = 'D&D: 5th Edition'
  return engine_title

@register.simple_tag
def split_range(array):
  if len(array) > 1:
    x,y = array
    r = str(x) + '-' + str(y)
  else:
    r = array[0]
  return str(r)

# Stat modifiers
@register.simple_tag
def stat_mod(stat, array):
  if stat in array:
    statMod = 2
    return statMod
  else:
    statMod = 0
    return statMod
