import datetime
from django.test import TestCase, Client
from django.urls import reverse
import smb.models as m

# Globals
CLIENT = Client()

# Mech Views
class TestMechViews(TestCase):

  def setUp(self):
    self.index = reverse('smb:index')
    self.dossier1 = reverse('smb:dossier', args=[100001])
    self.dossier2 = reverse('smb:dossier', args=[999999])

    self.mech_class1 = m.MechClass.objects.create(
      name='MechClassOne',
      base_strength = 3,
      base_defense = 2,
      base_dexterity = 1,
      base_hull = 0,
      base_repair_kits = 0,
      base_shields = 0,
      base_skill_points = 0
    )
    
    self.mech1 = m.Mech.objects.create(
      name='CharacterOne',
      mech_id=100001,
      mech_class_id=1,
      strength = 3,
      defense = 2,
      dexterity = 1,
      hull = 0,
      repair_kits = 0,
      shields = 0,
      skill_points = 0
    )

  def test_index_GET(self):
    response = CLIENT.get(self.index)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'smb/index.html')

  def test_dossier_GET(self):

    ## Test response to valid mech_id
    response1 = CLIENT.get(self.dossier1)
    self.assertEquals(response1.status_code, 200, 'This mech_id should register as valid.')
    self.assertTemplateUsed(response1, 'smb/mech/dossier.html')

    ## Test response to invalid mech_id
    response2 = CLIENT.get(self.dossier2)
    self.assertEquals(response2.status_code, 404, 'This mech_id should register as invalid.')
