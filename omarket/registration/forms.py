from django import forms

#
# model dependencies 
#
from address.models import Country, City

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


PASSWORD_MIN_LENGTH = 8
MAX_USERNAME_LENGTH = 150

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
    email = forms.EmailField( required = True,
                              max_length = MAX_USERNAME_LENGTH,
                              widget=forms.EmailInput( attrs={'placeholder': 'myemail@mail.com'}))
    passwordSignup = forms.CharField( required = True,
                                      min_length = PASSWORD_MIN_LENGTH,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'X8df!90EO'}))
    confirmPassword = forms.CharField( required = True,
                                       min_length = PASSWORD_MIN_LENGTH,
                                       widget=forms.PasswordInput(attrs={'placeholder': 'X8df!90EO'}))                                                 
    countrySignup = forms.ChoiceField( choices = getCountryCodeCountryTuples())
    citySignup = forms.ChoiceField( choices = [])
     
    


                       
