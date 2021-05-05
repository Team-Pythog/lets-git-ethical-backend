from django.db import models
from django.contrib.auth import get_user_model

class Dilemmas(models.Model):
  title = models.CharField(max_length=64)
  image = models.ImageField(upload_to='ethics_app/image_assets')
  dilemma = models.TextField()
  # responses = 4x models.CharField(max_length=64, null=True)

  def __str__(self):
    return self.title