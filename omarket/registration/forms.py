from django import forms
from phonenumber_field.formfields import PhoneNumberField

#
# model dependencies 
#
from address.models import Country, City


#
# US States hardcoded
#
STATES_US_CHOICES = [ (1, 'AL'),(11, 'HI'),(21, 'MA'),(31, 'NM'),(41, 'SD'),
                      (2, 'AK'),(12, 'ID'),(22, 'MI'),(32, 'NY'),(42, 'TN'),
                      (3, 'AZ'),(13, 'IL'),(23, 'MN'),(33, 'NC'),(43, 'TX'),
                      (4, 'AR'),(14, 'IN'),(24, 'MS'),(34, 'ND'),(44, 'UT'),
                      (5, 'CA'),(15, 'IA'),(25, 'MO'),(35, 'OH'),(45, 'VT'),
                      (6, 'CO'),(16, 'KS'),(26, 'MT'),(36, 'OK'),(46, 'VA'),
                      (7, 'CT'),(17, 'KY'),(27, 'NE'),(37, 'OR'),(47, 'WA'),
                      (8, 'DE'),(18, 'LA'),(28, 'NV'),(38, 'PA'),(48, 'WV'),
                      (9, 'FL'),(19, 'ME'),(29, 'NH'),(39, 'RI'),(49, 'WI'),
                      (10,'GA'),(20, 'MD'),(30, 'NJ'),(40, 'SC'),(50, 'WY') ]
                      
                      

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
ADDRESS_MAX_LENGTH = 500

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
    citySignup = forms.ChoiceField( choices = [])
    stateSignup = forms.ChoiceField( choices = STATES_US_CHOICES )
    addressSignup = forms.CharField( max_length = ADDRESS_MAX_LENGTH,
                                     widget=forms.TextInput(attrs={'placeholder':'235 Albany St. APT #2005'}))
     
    mobileNumberSignup = PhoneNumberField()


                       
