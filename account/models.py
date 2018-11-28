"""
131072
231118 - initial
account/forms.py



"""


# =============

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default = 'profile_pics/46761582_183035712641249_1139093754318159872_n.jpg' , upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

