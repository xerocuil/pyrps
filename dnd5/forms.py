from django.forms import ModelForm, NumberInput, Textarea
from .models import Cclass, Character

class CclassForm(ModelForm):
  class Meta:
    model = Cclass
    fields = ['name', 'description', 'hit_die', 'primary', 'stp', 'awp']

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = [
      'name',
      'level',
      'cclass',
      'bio',
      'strength',
      'dexterity',
      'constitution',
      'intelligence',
      'wisdom',
      'charisma',
      'weapon_main',
      'weapon_secondary',
      'armor',
      'shield',
      'race',
    ]
    widgets = {
      'level' : NumberInput(attrs={'class': 'integer'}),
      'strength' : NumberInput(attrs={'class': 'integer'}),
      'dexterity' : NumberInput(attrs={'class': 'integer'}),
      'constitution' : NumberInput(attrs={'class': 'integer'}),
      'intelligence' : NumberInput(attrs={'class': 'integer'}),
      'wisdom' : NumberInput(attrs={'class': 'integer'}),
      'charisma' : NumberInput(attrs={'class': 'integer'}),
    }

class AvatarForm(ModelForm):
  class Meta:
    model = Character
    fields = ['avatar']