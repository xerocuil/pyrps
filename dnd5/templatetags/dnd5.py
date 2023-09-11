from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

register = template.Library()

@register.simple_tag
def engine_title():
  engine_title = 'D&D: 5th Edition'
  return engine_title

# Stat modifiers
@register.simple_tag
def stat_mod(stat, array):
  if stat in array:
    statMod = 2
    return statMod
  else:
    statMod = 0
    return statMod
