import os
import sys
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

register = template.Library()

# Engine title
@register.simple_tag
def engine_title():
  engine_title = 'Super Mech Battle'
  return engine_title