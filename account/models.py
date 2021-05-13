from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class Profile(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='images/profile')
    header = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='user')
    bio = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return str(self.user.username)
    
    def get_absolute_url(self):
        return "/users/{}".format(self.slug)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)    
