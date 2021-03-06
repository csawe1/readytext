from django.db import models
#from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Waitlist(models.Model):
    wait = models.IntegerField()
    party_name = models.CharField(max_length=20)
    size = models.IntegerField()
    #phone = PhoneField()
    #E164_only=False if numbers are from US only.
    phone = PhoneNumberField()
    note = models.CharField(max_length=20, null=True, blank=True)
    state = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.party_name

class Message(models.Model):
    message_number = models.IntegerField()
    message_text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

