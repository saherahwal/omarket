from django.db import models
from django.contrib.auth.models import User

"""

Module: Registration and Subscription

Author: Saher Ahwal
Date:   Nov. 2014

"""

## Define Globals here
PHONE_LENGTH = 13
NAME_LENGTH = 100

# Create your models here.

class SubscriptionType(models.Model):
    """ this is the site subscription - depends on premium acccount payment """
    subscription_type_name = models.CharField(max_length=NAME_LENGTH)
    subscription_description = models.TextField()

class UserProfile(User):
    """ inherits from AbstractUser in Django - mainly used for authentication"""
    # other fields here
    phone = models.CharField(max_length=PHONE_LENGTH)  #optional
    mobile = models.CharField(max_length=PHONE_LENGTH) #requried 

    # foreign key
    subscription_type = models.ForeignKey(SubscriptionType)
    
    def __str__(self):
        return "%s's profile" % self.user

