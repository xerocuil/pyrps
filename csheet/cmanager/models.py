import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from PIL import Image

class Player(models.Model):
	name = models.CharField(max_length=128, unique=True)
	rank = models.IntegerField(default=1)
	tagline = models.CharField(max_length=1024 ,blank=True, null=True)
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Mech(models.Model):
	name = models.CharField(max_length=128, unique=True)
	pilot = models.ForeignKey('Player', blank=True, null=True, on_delete=models.CASCADE)
	mech_class = models.ForeignKey('MechClass', blank=True, null=True, on_delete=models.CASCADE)
	mod_strength = models.IntegerField(default=0)
	mod_defense = models.IntegerField(default=0)
	mod_dexterity = models.IntegerField(default=0)
	mod_endurance = models.IntegerField(default=0)
	mod_potions = models.IntegerField(default=0)
	mod_shields = models.IntegerField(default=0)
	mod_skill_points = models.IntegerField(default=0)

	def __str__(self):
		return self.name

	def hitpoints(self):
		basehp =  int(((9 + int(self.mech_class.base_endurance))/10) * 1000)
		totalhp = int(basehp) + (int(self.mod_endurance) * 100)
		return totalhp

	def potions_range(self):
		t = (int(self.mech_class.base_potions) + int(self.mod_potions))
		r = range(0,int(t),1)
		return r

	def total_potions(self):
		return (int(self.mech_class.base_potions) + int(self.mod_potions))

	def shields_range(self):
		t = (int(self.mech_class.base_potions) + int(self.mod_potions))
		r = range(0,int(t),1)
		return r

	def total_shields(self):
		return (int(self.mech_class.base_shields) + int(self.mod_shields))

	def skill_points_range(self):
		t = (int(self.mech_class.base_skill_points) + int(self.mod_skill_points))
		r = range(0,int(t),1)
		return r

	def total_skill_points(self):
		return (int(self.mech_class.base_skill_points) + int(self.mod_skill_points))

	def spent_skill_points(self):
		modifiers = (self.mod_strength, self.mod_defense, self.mod_dexterity, self.mod_endurance, self.mod_potions, self.mod_shields, self.mod_skill_points)
		modifier_total = sum(modifiers)
		return modifier_total

	def available_skill_points(self):
		a = int(self.pilot.rank) - int(self.spent_skill_points())
		return a

	def strength_range(self):
		str_range = range(0,self.mech_class.base_strength,1)
		return str_range

	def defense_range(self):
		def_range = range(0,self.mech_class.base_defense,1)
		return def_range

	def dexterity_range(self):
		dex_range = range(0,self.mech_class.base_dexterity,1)
		return dex_range

	def melee_attack_min(self):
		m = (((self.mech_class.base_strength * 1) + self.mod_strength) * 10)
		return m

	def melee_attack_max(self):
		m = (((self.mech_class.base_strength * 6) + self.mod_strength) * 10)
		return m

class MechClass(models.Model):
	name = models.CharField(max_length=128, unique=True)
	base_strength = models.IntegerField(default=2)
	base_defense = models.IntegerField(default=2)
	base_dexterity = models.IntegerField(default=2)
	base_endurance = models.IntegerField(default=1)
	base_potions = models.IntegerField(default=4)
	base_shields = models.IntegerField(default=4)
	base_skill_points = models.IntegerField(default=4)

	class Meta:
		ordering = ["name"]
		verbose_name = "Mech Class"
		verbose_name_plural = "Mech Classes"

	def __str__(self):
		return self.name

class Page(models.Model):
	title = models.CharField(max_length=128, unique=True)
	slug = models.CharField(max_length=64, unique=True)
	content = models.TextField(blank=True, null=True)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.title
