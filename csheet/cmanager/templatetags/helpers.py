from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag()
def appName():
	name = 'Super Mech Battle!'
	return mark_safe(name)

@register.simple_tag()
def baseStat():
	button = '<img class="stat-icon" src="/static/images/1d6.png" title="Base Stat">'
	return mark_safe(button)

@register.simple_tag()
def potion():
	button = '<img class="stat-icon" src="/static/images/potion.svg" title="Energy Potion">'
	return mark_safe(button)

@register.simple_tag()
def shield():
	button = '<img class="stat-icon" src="/static/images/shield.svg" title="Energy Shield">'
	return mark_safe(button)

@register.simple_tag()
def skill():
	button = '<img class="stat-icon" src="/static/images/skill.svg" title="Skill Point">'
	return mark_safe(button)