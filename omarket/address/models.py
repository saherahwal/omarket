from django.db import models

class Currency(models.Model):
    """ currency (e.g NIS, U.S. Dollars, JD)"""
    name = models.CharField(max_length = 70)
    code = models.CharField(max_length = 10)    

class Country(models.Model):
    country_name = models.CharField(max_length = 50)
    country_code = models.CharField(max_length = 2)
    phone_code = models.CharField(max_length = 3, default = '000')
    country_name_ar = models.CharField(max_length = 50, default = '')

     #many-to-many fields
    currencies = models.ManyToManyField(Currency)

class City(models.Model):
    city_name = models.CharField(max_length = 93)
    city_name_ar = models.CharField(max_length = 93, default = '')
    country = models.ForeignKey(Country)

class Address(models.Model):
    street_address = models.CharField(max_length = 350)
    city = models.ForeignKey(City) # country included implicitly in city
    zip_code = models.CharField(max_length = 5, default = '')

