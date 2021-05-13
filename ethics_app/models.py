from django.db import models
from django.contrib.auth.models import User

class Dilemmas(models.Model):
  id = models.BigAutoField(primary_key=True)
  title = models.CharField(max_length=64)
  image = models.ImageField(upload_to='images', blank=True)
  text = models.TextField()
  response_0 = models.CharField(max_length=64, blank=True, default='')
  response_1 = models.CharField(max_length=64, blank=True, default='')

  def __str__(self):
    return self.title