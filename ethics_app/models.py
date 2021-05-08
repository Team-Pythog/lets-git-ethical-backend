from django.db import models
from django.contrib.auth.models import User

class Dilemmas(models.Model):
  title = models.CharField(max_length=64)
  image = models.ImageField(upload_to='ethics_app/image_assets', blank=True)
  dilemma = models.TextField()
  # responses = models.Field
  # responses = 4x models.CharField(max_length=64, null=True)

  def __str__(self):
    return self.title

# class UserReg(models.Model):
#   username = models.CharField(max_length=32)
#   password = models.CharField(max_length=32)
#   email = models.EmailField(max_length=128)
  #  birth_date = models.DateField(null=True, blank=True)

class ProfileInfo(models.Model):
  thumbnail = models.ImageField(upload_to='ethics_app/image_assets', blank=True)
  header = models.CharField(max_length=64)
  header_image = models.ImageField(upload_to='ethics_app/image_assets', blank=True)
  bio = models.TextField()
  gender = models.CharField(max_length=32)
  instagram = models.URLField(max_length=200, blank=True)
  facebook = models.URLField(max_length=200, blank=True)
  linkedin = models.URLField(max_length=200, blank=True)

