from django.db import models

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from PIL import Image

from cmanager.models import Mech

class Campaign(models.Model):
	name = models.CharField(max_length=128, unique=True)
	mech = models.ManyToManyField(Mech)
	turn = models.IntegerField(default=0)

	def __str__(self):
		return self.name