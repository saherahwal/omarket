from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from registration import forms as regForms
from registration.models import SubscriptionType, UserProfile
#
# Localizable Strings
#
USER_VALID_AUTHENTICATED = "User is valid, active and authenticated"
USER_VALID_ACCOUNT_DISABLED = "Password valid, but account disabled"
AUTHENTICATION_FAIL = "Neither username nor email authentication worked. Password and/or username invalid"
USERNAME_ALREADY_EXISTS = "Username already exists, try another one"
EMAIL_ALREADY_EXISTS = "Email provided has already been registered"
PASSWORDS_DO_NOT_MATCH = "Passwords do not match"
ERRORS_IN_FORM = "Erros in Form. Did NOT submit"

def home(request):
    #
    # create the unbounded forms for registration
    #
    if request.method == 'GET':        
        loginForm =  regForms.LoginForm()
        signupForm = regForms.SignupForm()        
        return render(request,
                      "register.html",
                      {'loginForm': loginForm,
                       'signupForm' : signupForm })
    
def signin(request):
    #
    # Create unbounded signup form
    #
    signupForm = regForms.SignupForm()
    
    #
    # if post request then process form data
    #
    if request.method == 'POST':
        respErrors = []
        
        #
        # create form instance to process form data
        #
        loginForm = regForms.LoginForm(request.POST)
        
        #
        # check whether form is valid
        #
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            keepMeLoggedIn = loginForm.cleaned_data['keepMeLoggedIn']
           
            #
            # authenticate using email or username
            #
            (user, msg) = omarketAuth(username, password)
            if user is not None:
                #
                # redirect to login success page
                #
                #TODO: fill this in
                palcehold = "garbage"
            else:
                respErrors.append(msg)
                return render(request, "register.html", {'loginForm': loginForm,
                                                     'signupForm' : signupForm, 
                                                     'respErrors': respErrors })
        else:            
            #
            # if not valid form
            #
            #respErrors.append(ERRORS_IN_FORM)        
            return render(request, "register.html", {'loginForm': loginForm,
                                                     'signupForm' : signupForm, 
                                                     'respErrors': respErrors })
        
    elif request.method == 'GET':
        loginForm = regForms.LoginForm()
        return render(request, "register.html", {'loginForm': loginForm,
                                                 'signupForm' : signupForm})
    else:
        loginForm = regForms.LoginForm()
        return render(request, "register.html", {'loginForm': loginForm,
                                                 'signupForm' : signupForm})
  
def signup(request):
    #
    # Create unbounded login form
    #
    loginForm = regForms.LoginForm()

    print request.get_full_path()
    
    if request.method == 'POST':
        respErrorsSignup = []

        #
        # create singup form instance to process form data
        #
        signupForm = regForms.SignupForm(request.POST)

        if signupForm.is_valid():

            #
            # get form data
            #
            username = signupForm.cleaned_data['usernameSignup']
            email = signupForm.cleaned_data['emailSignup']
            password = signupForm.cleaned_data['passwordSignup']
            confirmPassword = signupForm.cleaned_data['confirmPasswordSignup']
            country = signupForm.cleaned_data['countrySignup']
            city = signupForm.cleaned_data['citySignup']
            state = signupForm.cleaned_data['stateSignup']
            mobile = signupForm.cleaned_data['mobileNumberSignup']
            subscriptiontype = signupForm.cleaned_data['subscriptionTypeSignup']

            #
            # Check if user exists already
            # NOTE: check both email and username as each is unique among data set
            #           
            if(usernameExists(username)):
                respErrorsSignup.append( USERNAME_ALREADY_EXISTS )

            if(emailExists(email)):
                respErrorsSignup.append( EMAIL_ALREADY_EXISTS )

            if password != confirmPassword:
                respErrorsSignup.append( PASSWORDS_DO_NOT_MATCH )

            #
            # if errors exist - return
            #
            if len(respErrorsSignup) != 0:
                return render(request, "register.html", {'loginForm': loginForm,
                                                         'signupForm' : signupForm,
                                                         'respErrorsSignup' : respErrorsSignup } )                
            #
            # Create user
            #
            user = UserProfile.objects.create_user(username=username,
                                                   password=password,
                                                   email=email,
                                                   mobile=mobile,
                                                   subscription_type=subscriptiontype)
            
            return render(request, "register.html", {'loginForm': loginForm,
                                                     'signupForm' : signupForm,
                                                     'respErrorsSignup' : respErrorsSignup } )  
        else:
            #
            # form invalid
            #
            #respErrorsSignup.append(ERRORS_IN_FORM)            
            return render(request, "register.html", {'loginForm': loginForm,
                                                     'signupForm' : signupForm,
                                                     'respErrorsSignup' : respErrorsSignup })  
    else:
        signupForm = regForms.SignupForm()
        return render(request, "register.html", {'loginForm': loginForm,                                              
                                                 'signupForm' : signupForm})
            
                                            
            
            
        


@login_required(login_url='/registration/signin/')
def signout(request):
    print "signing out"
    logout(request)
    return render (request, "login.html", {})

#
# helper methods
#
def usernameExists(username):
    user_username_count = UserProfile.objects.filter(username=username).count()
    return (user_username_count==1)

def emailExists(email):
    user_email_count = UserProfile.objects.filter(email=email).count()
    return (user_email_count==1)
   

#
# authentication helper methods
#
def authenticate_username(username, password):
    return authenticate(username=username, password=password)

def authenticate_email(email, password):
    try:
        user = UserProfile.objects.get(email__iexact=email)
        if user.check_password(password):
            return user
        return None
    except ObjectDoesNotExist:
        return None
     
def omarketAuth( username, password ):
    user = authenticate_username(username, password)
    user_email = authenticate_email(username, password)
    if user is not None:        
        if user.is_active:
            return (user, USER_VALID_AUTHENTICATED)
        else:
            return (None, USER_VALID_ACCOUNT_DISABLED)            
    elif user_email is not None:
        if user_email.is_active:
            return (user_email, USER_VALID_AUTHENTICATED)
        else:
            return (None, USER_VALID_ACCOUNT_DISABLED)
    else:
        return (None, AUTHENTICATION_FAIL)
        
        
