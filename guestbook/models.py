from django.db import models
from django.conf import settings

# Create your models here.
""""
131072
051018 - initial





"""


# =============

class TextMessage(models.Model):
    talker = models.CharField(max_length=20, blank=False)
    message = models.CharField(max_length=113, blank=True)

    def _str_(self):
        return self.talker + " " + self.message
