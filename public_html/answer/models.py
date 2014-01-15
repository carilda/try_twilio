from django.db import models

class Twilio(models.Model):
    owner = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=16)
    sid = models.CharField(max_length=50)
    token = models.CharField(max_length=50)

    def __unicode__(self):
        return self.owner + ": " + self.phone_number
    
