from django import template
from django.template.defaultfilters import stringfilter
from main.apps import MainConfig

register = template.Library()

@register.simple_tag
def app_title():
  return MainConfig.verbose_name
