import os
import sys
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from smb.apps import SmbConfig

register = template.Library()

# Engine title
@register.simple_tag
def engine_title():
  # engine_title = 'Super Mech Battle'
  return SmbConfig.verbose_name