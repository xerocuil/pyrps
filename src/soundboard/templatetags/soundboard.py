import os
import sys
import ffmpeg

from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.utils.safestring import mark_safe

from soundboard.apps import SoundboardConfig

register = template.Library()

# Engine title
@register.simple_tag
def engine_title():
  return SoundboardConfig.verbose_name

# Engine logo
@register.simple_tag
def engine_logo():
  logo_url = '/static/soundboard/img/icon.svg'
  return logo_url
