from django.db import models

class Soundboard(models.Model):
  name = models.CharField(max_length=255, unique=True)
  sfx1 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx1")
  sfx2 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx2")
  sfx3 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx3")
  sfx4 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx4")
  sfx5 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx5")
  sfx6 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx6")
  sfx7 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx7")
  sfx8 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx8")
  sfx9 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx9")
  sfx10 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx10")
  sfx11 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx11")
  sfx12 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx12")
  sfx13 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx13")
  sfx14 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx14")
  sfx15 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx15")
  sfx16 = models.ForeignKey('Sfx', blank=True, null=True, on_delete=models.CASCADE, related_name="sfx16")

  music1 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music1")
  music2 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music2")
  music3 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music3")
  music4 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music4")
  music5 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music5")
  music6 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music6")
  music7 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music7")
  music8 = models.ForeignKey('Music', blank=True, null=True, on_delete=models.CASCADE, related_name="music8")

  ''' Meta '''
  class Meta:
    ordering = ["name"]

  def __str__(self):
    return self.name
  

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