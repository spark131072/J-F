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
    image = models.ImageField(default='profile_pics/JFBLK.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Geo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=113, blank=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.lat) + str(self.lng)


class Taste(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=113, blank=False)
    self_atc = models.DecimalField(max_digits=2, decimal_places=1)
    self_amb = models.DecimalField(max_digits=2, decimal_places=1)
    self_fun = models.DecimalField(max_digits=2, decimal_places=1)
    self_int = models.DecimalField(max_digits=2, decimal_places=1)
    self_sin = models.DecimalField(max_digits=2, decimal_places=1)
    prtn_atc = models.DecimalField(max_digits=2, decimal_places=1)
    prtn_amb = models.DecimalField(max_digits=2, decimal_places=1)
    prtn_fun = models.DecimalField(max_digits=2, decimal_places=1)
    prtn_int = models.DecimalField(max_digits=2, decimal_places=1)
    prtn_sin = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return str(self.user_id) + "," + str(self.username) + "," +\
str(self.self_atc) + "," + str(self.self_amb) + "," +\
str(self.self_fun) + "," + str(self.self_int) + "," + str(self.self_sin) + "," +\
str(self.prtn_atc) + "," + str(self.prtn_amb) + "," +\
str(self.prtn_fun) + "," + str(self.prtn_int) + "," + str(self.prtn_sin)
