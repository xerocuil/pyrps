from django.db import models


  

class Sfx(models.Model):
  name = models.CharField(max_length=128, unique=True)
  file = models.FileField(upload_to='soundboard/sfx',
    blank=True, null=True)

  ''' Meta '''
  class Meta:
    ordering = ["name"]
    verbose_name = "SFX"
    verbose_name_plural = "SFX"

  def __str__(self):
    return self.name


class Music(models.Model):
  name = models.CharField(max_length=128, unique=True)
  file = models.FileField(upload_to='soundboard/music',
    blank=True, null=True)

  ''' Meta '''
  class Meta:
    ordering = ["name"]
    verbose_name = "Music"
    verbose_name_plural = "Music"

  def __str__(self):
    return self.name


class Soundboard(models.Model):
  name = models.CharField(max_length=255, unique=True)
  sfx = models.ManyToManyField(Sfx)
  music = models.ManyToManyField(Music)

  ''' Meta '''
  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name