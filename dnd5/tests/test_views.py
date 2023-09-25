import datetime
from django.test import TestCase, Client
from django.urls import reverse
import dnd5.models as m

# Globals
CLIENT = Client()

# Character Views
class TestCharacterViews(TestCase):

  def setUp(self):
    self.index = reverse('dnd5:index')
    self.character_sheet1 = reverse('dnd5:character_sheet', args=[100001])
    self.character_sheet2 = reverse('dnd5:character_sheet', args=[999999])
    self.list_characters = reverse('dnd5:list_characters')
    self.add_char = reverse('dnd5:add_char')
    # self.edit_char = reverse('dnd5:edit_char')
    
    self.class1 = m.Cclass.objects.create(
      name='ClassOne',
      hit_die = 12
    )
    
    self.char1 = m.Character.objects.create(
      name='CharacterOne',
      charid=100001,
      cclass_id=1
    )

    self.char_list = m.Character.objects.all()


  def test_index_GET(self):
    response = CLIENT.get(self.index)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'dnd5/index.html')


  def test_add_char_GET(self):
    response = CLIENT.get(self.add_char)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'dnd5/character/add.html')


  def test_add_char_POST(self):

    ''' Attempt valid entry '''
    response1 = CLIENT.post(self.add_char, {
      'name': 'CharacterTwo',
      'level': 1,
      'strength': 1,
      'dexterity': 1,
      'constitution': 1,
      'intelligence': 1,
      'wisdom': 1,
      'charisma': 1,
      'inspiration': 1,
      'date_added': datetime.datetime.now(),
      'date_modified': datetime.datetime.now(),
    })

    self.assertEquals(response1.status_code, 302)
    self.assertEquals(self.char_list[0].name, 'CharacterOne')
    self.assertEquals(self.char_list[1].name, 'CharacterTwo')

    
    ''' Attempt invalid entry '''
    response2 = CLIENT.post(self.add_char, {
      'name': 'CharacterX',
      'level': 'X',
      'strength': 1,
      'dexterity': 1,
      'constitution': 1,
      'intelligence': 1,
      'wisdom': 1,
      'charisma': 1,
      'inspiration': 1,
      'date_added': datetime.datetime.now(),
      'date_modified': datetime.datetime.now(),
    })

    for i in self.char_list:
      if i.name == 'CharacterX':
        data_type = False
      else:
        data_type = True

    self.assertTrue(data_type, '')


  def test_character_sheet_GET(self):

    ## Test response to valid charid
    response1 = CLIENT.get(self.character_sheet1)
    self.assertEquals(response1.status_code, 200, 'This charid should register as valid.')
    self.assertTemplateUsed(response1, 'dnd5/character/sheet.html')

    ## Test response to invalid charid
    response2 = CLIENT.get(self.character_sheet2)
    self.assertEquals(response2.status_code, 404, 'This charid should register as invalid.')


  def test_list_characters_GET(self):
    response = CLIENT.get(self.list_characters)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'dnd5/character/list.html')
