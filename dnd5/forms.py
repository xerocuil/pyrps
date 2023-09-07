from django.forms import ModelForm
from .models import Cclass, Character

class CclassForm(ModelForm):
  class Meta:
    model = Cclass
    fields = ['name', 'description', 'hit_die', 'primary', 'stp', 'awp']

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = ['name', 'level', 'cclass', 'bio', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    # fields = "__all__"

class AvatarForm(ModelForm):
  class Meta:
    model = Character
    fields = ['avatar']