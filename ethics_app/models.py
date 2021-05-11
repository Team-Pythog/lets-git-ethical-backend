from django.db import models
from django.contrib.auth.models import User

class Dilemmas(models.Model):
  title = models.CharField(max_length=64)
  image = models.ImageField(upload_to='images', blank=True)
  text = models.TextField()
  response_0 = models.CharField(max_length=64, blank=True, default='')
  response_1 = models.CharField(max_length=64, blank=True, default='')

  def __str__(self):
    return self.title

class ProfileInfo(models.Model):
  image = models.ImageField(upload_to='ethics_app/image_assets', blank=True)
  header = models.CharField(max_length=64)
  banner = models.ImageField(upload_to='ethics_app/image_assets', blank=True)
  bio = models.TextField()
  gender = models.CharField(max_length=32)
  instagram = models.URLField(max_length=200, blank=True)
  facebook = models.URLField(max_length=200, blank=True)
  linkedin = models.URLField(max_length=200, blank=True)


