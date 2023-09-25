from django.test import SimpleTestCase
from django.urls import resolve, reverse
import dnd5.views as v

class TestUrls(SimpleTestCase):

  def test_index(self):
    url = reverse('dnd5:index')
    self.assertEquals(resolve(url).func, v.index)

  def test_add_char(self):
    url = reverse('dnd5:add_char')
    self.assertEquals(resolve(url).func, v.add_char)

  def test_character_sheet(self):
    url = reverse('dnd5:character_sheet', args=[2])
    self.assertEquals(resolve(url).func, v.character_sheet)
