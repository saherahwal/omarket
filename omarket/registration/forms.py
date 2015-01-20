from django import forms
from phonenumber_field.formfields import PhoneNumberField

#
# model dependencies 
#
from address.models import Country, City
from registration.models import SubscriptionType


#
# US States hardcoded
#
STATES_US_CHOICES = [(1, 'AL'), (2, 'AK'), (3, 'AZ'), (4, 'AR'), (5, 'CA'),
                     (6, 'CO'), (7, 'CT'), (8, 'DE'), (9, 'FL'), (10, 'GA'),
                     (11, 'HI'), (12, 'ID'), (13, 'IL'), (14, 'IN'), (15, 'IA'),
                     (16, 'KS'), (17, 'KY'), (18, 'LA'), (19, 'ME'), (20, 'MD'),
                     (21, 'MA'), (22, 'MI'), (23, 'MN'), (24, 'MS'), (25, 'MO'),
                     (26, 'MT'), (27, 'NE'), (28, 'NV'), (29, 'NH'), (30, 'NJ'),
                     (31, 'NM'), (32, 'NY'), (33, 'NC'), (34, 'ND'), (35, 'OH'),
                     (36, 'OK'), (37, 'OR'), (38, 'PA'), (39, 'RI'), (40, 'SC'),
                     (41, 'SD'), (42, 'TN'), (43, 'TX'), (44, 'UT'), (45, 'VT'),
                     (46, 'VA'), (47, 'WA'), (48, 'WV'), (49, 'WI'), (50, 'WY')]  

PASSWORD_MIN_LENGTH = 8
MAX_USERNAME_LENGTH = 150
ADDRESS_MAX_LENGTH = 500
MAX_CITYNAME_LENGTH=93
MAX_ZIPCODE_LENGTH=5
#
# Helper Functions
#
def getCountryCodeCountryTuples():
    """
        return a list of 2-tuples of country-code and country_name
    """
    countryQuerySet = Country.objects.all().order_by('country_name')
    listRes = []
    for q in countryQuerySet:
        tupRes = ( q.id, q.country_name)
        listRes.append( tupRes)
    return listRes

def getStateFromId(idNum):
    for s in STATES_US_CHOICES:
        if( s[0] == idNum ):
            return s[1]

    

class LoginForm(forms.Form):
    username = forms.CharField( required = True,
                                max_length=MAX_USERNAME_LENGTH,                                
                                widget=forms.TextInput(attrs={'placeholder': 'myusername or myemail@mail.com'}))
    password = forms.CharField( required = True,
                                min_length = PASSWORD_MIN_LENGTH,
                                widget=forms.PasswordInput(attrs={'placeholder': 'X8df!90EO'}))     
    keepMeLoggedIn = forms.BooleanField( required = False)    


class SignupForm(forms.Form):
    usernameSignup = forms.CharField( required = True,
                                      max_length = MAX_USERNAME_LENGTH,
                                      widget=forms.TextInput(attrs={'placeholder': 'mysuperusername631'}))
    emailSignup = forms.EmailField( required = True,
                                    max_length = MAX_USERNAME_LENGTH,
                                    widget=forms.EmailInput( attrs={'placeholder': 'myemail@mail.com'}))
    passwordSignup = forms.CharField( required = True,
                                      min_length = PASSWORD_MIN_LENGTH,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'X8df!90EO'}))
    confirmPasswordSignup = forms.CharField( required = True,
                                             min_length = PASSWORD_MIN_LENGTH,
                                             widget=forms.PasswordInput(attrs={'placeholder': 'X8df!90EO'}))                                                 
    countrySignup = forms.ChoiceField( choices = getCountryCodeCountryTuples())
    citySignup = forms.CharField(required = True,
                                 max_length=MAX_CITYNAME_LENGTH,
                                 widget=forms.TextInput(attrs={'placeholder': 'e.g Chicago'}))                                 
    zipcodeSignup = forms.CharField(required=False,
                                    max_length=MAX_ZIPCODE_LENGTH)                                
    stateSignup = forms.ChoiceField( required = False,
                                     choices = STATES_US_CHOICES )
    addressSignup = forms.CharField( max_length = ADDRESS_MAX_LENGTH,
                                     widget=forms.TextInput(attrs={'placeholder':'235 Albany St. APT #2005'}))
    mobileNumberSignup = PhoneNumberField()
    subscriptionTypeSignup = forms.ModelChoiceField(queryset= SubscriptionType.objects.all() ,
                                                    empty_label=None)

class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField( required = True,
                                   min_length = PASSWORD_MIN_LENGTH,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'X8df!90EO'}))
    newPassword = forms.CharField( required = True,
                                   min_length = PASSWORD_MIN_LENGTH,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'W9va!80FQ'}))
    confirmNewPassword = forms.CharField( required = True,
                                          min_length = PASSWORD_MIN_LENGTH,
                                          widget=forms.PasswordInput(attrs={'placeholder': 'W9va!80FQ'}))

                       
