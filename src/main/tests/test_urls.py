from django.test import SimpleTestCase
from django.urls import resolve, reverse
import main.views as v

class TestUrls(SimpleTestCase):

  def test_index(self):
    url = reverse('main:index')
    self.assertEquals(resolve(url).func, v.index)
