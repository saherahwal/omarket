from django import forms
from phonenumber_field.formfields import PhoneNumberField
from address.utils import *

from business.models import BusinessType

#
# model dependencies 
#

MAX_NAME_LENGTH = 100
MAX_TITLE_LENGTH = 60
MAX_VENDOR_LENGTH = 30
MAX_CATEGORY_LENGTH = 50
MAX_TYPE_LENGTH = 60
MAX_TAGS_LENGTH = 2000

#
# Helper Functions
#
def getCurreciesTuples():
    """
        return a list of 2-tuples of currency-code and name
    """
    return [ ('New Israeli Shiekel','NIS'), ('US Dollar', 'USD'), ('Euro', 'Euro'), ('Jordanian Dinars', 'JD') ]

def getShoppingCategoryTuples():
    """
        returns list of 2-tuples of shopping category IDs and names
    """
    return [ (1, 'Food'), (2, 'Beverage'), ( 3, 'Electronics') ]

def getBusinessTypeTuples():
    """
        return list of 2-tuples of business type IDs and names        
    """
    bussinessTypeQSet = BusinessType.objects.all().order_by('type_name')
    listRes = []
    for e in bussinessTypeQSet:        
        tupRes = ( e.id, e.type_name)
        listRes.append( tupRes )
    return listRes        

#
# Forms start here
#

class BusinessForm(forms.Form):
    name = forms.CharField( required = True,
                             max_length=MAX_NAME_LENGTH,                                
                             widget=forms.TextInput(attrs={'placeholder': 'e.g Boston Market'}))
    phone = PhoneNumberField()
    image = forms.ImageField()
    businessType = forms.ChoiceField( choices = getBusinessTypeTuples() )
    description = forms.CharField( widget=forms.Textarea )
    country = forms.ChoiceField( choices = getCountryCodeCountryTuples())
    city = forms.CharField(required = True,
                           max_length=MAX_CITYNAME_LENGTH,
                           widget=forms.TextInput(attrs={'placeholder': 'e.g Seattle'}))                                 
    zipcode = forms.CharField(required=False,
                              max_length=MAX_ZIPCODE_LENGTH)                                
    state = forms.ChoiceField( required = False,
                               choices = STATES_US_CHOICES )
    address = forms.CharField( max_length = ADDRESS_MAX_LENGTH,
                               widget=forms.TextInput(attrs={'placeholder':'362 Memorial Drive. APT #201'}))
    


class ItemAddForm(forms.Form):
    title = forms.CharField( required = True,
                             max_length=MAX_TITLE_LENGTH,                                
                             widget=forms.TextInput(attrs={'placeholder': 'e.g Microsoft Lumia 430 Phone'}))
    productType = forms.CharField( required = True,
                                   max_length=MAX_TYPE_LENGTH,                                
                                   widget=forms.TextInput(attrs={'placeholder': 'e.g T-shirts, Devices, Cakes'}))
    vendor = forms.CharField( required = False,
                             max_length=MAX_VENDOR_LENGTH,                                
                             widget=forms.TextInput(attrs={'placeholder': 'e.g Microsoft, Google, Lenovo'}))
    description = forms.CharField (widget=forms.Textarea)
    chargeTaxes = forms.BooleanField( required = False )
    shippingRequired = forms.BooleanField( required = False )
    price = forms.CharField( required = True,                                                         
                             widget=forms.NumberInput())
    tags = forms.CharField( required = True,
                            max_length=MAX_TAGS_LENGTH,                                
                            widget=forms.TextInput(attrs={'placeholder': 'e.g summer, silk, communication'}))
    currency = forms.ChoiceField( choices = getCurreciesTuples() )
    shoppingCategory = forms.ChoiceField( choices = getShoppingCategoryTuples() )
    newCategory = forms.CharField( required = False,
                                   max_length=MAX_CATEGORY_LENGTH,                                
                                   widget=forms.TextInput(attrs={'placeholder': 'e.g Dessert Menu, Shoe List, Wines'}))
    image = forms.ImageField()

class ServiceAddForm(forms.Form):
    title = forms.CharField( required = True,
                             max_length=MAX_TITLE_LENGTH,
                             widget=forms.TextInput(attrs={'placeholder': 'e.g House Cleaning, Suit Dry Clean ... '}))
    serviceType = forms.CharField( required = True,
                                   max_length=MAX_TYPE_LENGTH,                                
                                   widget=forms.TextInput(attrs={'placeholder': 'e.g Cleaning, Transportation, Utility'}))
    description = forms.CharField( widget=forms.Textarea )
    chargeTaxes = forms.BooleanField( required = False )
    price = forms.CharField( required = True,                                                         
                             widget=forms.NumberInput())
    tags = forms.CharField( required = True,
                            max_length=MAX_TAGS_LENGTH,                                
                            widget=forms.TextInput(attrs={'placeholder': 'e.g transportation, utilities, gardening'}))
    


##TODO: Taxi service special
class TaxiServiceForm(forms.Form):
    title = forms.CharField( required = True,
                             max_length=MAX_TITLE_LENGTH,
                             widget=forms.TextInput(attrs={'placeholder': 'e.g 7-passenger car, limo'}))
    description = forms.CharField (widget=forms.Textarea)
    tags = forms.CharField( required = True,
                            max_length=MAX_TAGS_LENGTH,                                
                            widget=forms.TextInput(attrs={'placeholder': 'e.g wedding, taxi, '}))

    

















    
