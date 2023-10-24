import os
from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=128, unique=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  ''' Meta '''
  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name


class Sfx(models.Model):
  name = models.CharField(max_length=128, unique=True)
  file = models.FileField(upload_to='soundboard/sfx',
    blank=True, null=True)
  tags = models.ManyToManyField(Tag, blank=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

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
  loop = models.BooleanField(default=False)
  tags = models.ManyToManyField(Tag, blank=True)
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  def get_filename(self):
    return os.path.basename(self.file.url)

  def get_format(self):
    file = os.path.basename(self.file.url)
    file = file.split('.')
    return file[1].upper()

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
  date_added = models.DateTimeField('Date Added', auto_now_add=True)

  ''' Meta '''
  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name
