from django.db import models

class Dilemmas(models.Model):
  id = models.BigAutoField(primary_key=True, null=False, default=-1)
  title = models.CharField(max_length=64, unique=True, blank=False)
  image = models.ImageField(upload_to='images', blank=True)
  text = models.TextField(blank=False)
  response_0 = models.CharField(max_length=128, blank=False)
  response_1 = models.CharField(max_length=128, blank=False)