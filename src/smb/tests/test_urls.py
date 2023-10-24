from django.test import SimpleTestCase
from django.urls import resolve, reverse
import smb.views as v

class TestUrls(SimpleTestCase):

  def test_index(self):
    url = reverse('smb:index')
    self.assertEquals(resolve(url).func, v.index)

  def test_dossier(self):
    url = reverse('smb:dossier', args=[2])
    self.assertEquals(resolve(url).func, v.dossier)
