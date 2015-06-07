"""

Module: Registration and Subscription

Author: Saher Ahwal
Date:   Nov. 2014

"""
from django.db import models

from registration.models import UserProfile
from address.models import Address, Currency

#
# upload-to DIR
#
UPLOAD_TO = 'business/images/'

## Define Globals here
NAME_LENGTH = 60
BUS_NAME_LENGTH = 60
PHONE_LENGTH = 13

class BusinessType(models.Model):    
    type_name = models.CharField(max_length=NAME_LENGTH)   
    type_name_ar = models.CharField(max_length = NAME_LENGTH)

class PricingType(models.Model):
    """ pricing type: (e.g fixed, range, dynamic)"""
    type_name = models.CharField(max_length=NAME_LENGTH)   
    type_name_ar = models.CharField(max_length = NAME_LENGTH)

class DeliveryType(models.Model):
    """ describes delivery choice for business e.g (own, third party, Omarket)"""
    type_name = models.CharField(max_length=NAME_LENGTH)   
    type_name_ar = models.CharField(max_length = NAME_LENGTH)

class Business(models.Model):
    """ Describes Bussines data type """    
    name = models.CharField(max_length=BUS_NAME_LENGTH)
    phone = models.CharField(max_length = PHONE_LENGTH)    
    
    img = models.ImageField( upload_to = UPLOAD_TO )
    
    offers_left = models.PositiveSmallIntegerField()
    business_description = models.TextField()
    num_customers = models.IntegerField()

    date_created = models.DateTimeField( auto_now_add = True )
    date_lmt = models.DateTimeField( auto_now = True )

    # foreign keys
    owner = models.ForeignKey(UserProfile, related_name="owner")    
    business_type = models.ForeignKey(BusinessType)   
        
    # many-to-many fields
    subscribers = models.ManyToManyField(UserProfile, related_name="subscribers")
    currencies = models.ManyToManyField(Currency, related_name="currencies")    
    addresses = models.ManyToManyField(Address)

class ShoppingCategory(models.Model):
    """ describes a shopping category (e.g Food, Toys, Office Accessories...etc) """
    category_name = models.CharField(max_length = NAME_LENGTH)
    category_name_ar = models.CharField(max_length = NAME_LENGTH)

    # foreign keys
    business = models.ForeignKey(Business)
    delivery_type = models.ForeignKey(DeliveryType) # (e.g None, Own, third-party)

class Vendor(models.Model):
    """ describes vendor list """
    name = models.CharField(max_length = NAME_LENGTH)

class ProductItem(models.Model):
    """ describes an item (physical product) """
    title = models.CharField( max_length = NAME_LENGTH )
    productType = models.CharField( max_length = NAME_LENGTH )
    description = models.TextField()
    chargeTaxes = models.BooleanField()
    shippingRequired = models.BooleanField()
    tags = models.TextField()
    mainImage = models.ImageField( upload_to='items' )    

    date_created = models.DateTimeField( auto_now_add = True )
    date_lmt = models.DateTimeField( auto_now = True )    
    
    # foreign keys
    vendor = models.ForeignKey( Vendor )
    currency = models.ForeignKey( Currency )
    shoppingCategory = models.ForeignKey( ShoppingCategory )

class ProductImage(models.Model):
    """ stores image urls for multiple image support for items """
    img = models.ImageField( upload_to='items' )

    # foreign keys
    productItem = models.ForeignKey( ProductItem )

##TODO: service items

class ServiceItem(models.Model):
    """ describes Service item """
    title = models.CharField( max_length = NAME_LENGTH )
    serviceType = models.CharField( max_length = NAME_LENGTH )
    description = models.TextField()

    # foreign keys
    pricingType = models.ForeignKey( PricingType )
    
    
    
   
    
    
    

    

    
    
    
    
