from django import forms
from phonenumber_field.formfields import PhoneNumberField

#
# model dependencies 
#
from address.models import Country, City
from registration.models import SubscriptionType
from address.utils import *

PASSWORD_MIN_LENGTH = 8
MAX_USERNAME_LENGTH = 150

#
# Forms start here
#

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

                       
