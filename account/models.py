from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True)
    header = models.CharField(max_length=64, blank=True)
    bio = models.CharField(max_length=300, blank=True)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)    
