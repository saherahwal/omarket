from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from registration import forms as regForms

def home(request):
    #
    # create the unbounded forms for registration
    #
    if request.method == 'GET':        
        loginForm =  regForms.LoginForm()
        signupForm = regForms.SignupForm()        
        return render(request,
                      "login.html",
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
                pass
            else:
                respErrors.append(msg)                            
        return render(request, "login.html", {'loginForm': loginForm,
                                              'signupForm' : signupForm, 
                                              'respErrors': respErrors }) 
        
    elif request.method == 'GET':
        loginForm = regForms.LoginForm()
        return render(request, "login.html", {'loginForm': loginForm,
                                              'signupForm' : signupForm})
    else:
        loginForm = regForms.LoginForm()
        return render(request, "login.html", {'loginForm': loginForm,
                                              'signupForm' : signupForm})
  
def signup(request):
    #
    # Create unbounded login form
    #
    loginForm = regForms.LoginForm()
    
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

            #
            # Create user object
            #
            
            
        
##        errorMsg = "success"
##        if 'username_signup' in request.POST and \
##           'email_signup' in request.POST and \
##           'password_signup' in request.POST and \
##           'password_confirm_signup' in request.POST:
##            
##            username = request.POST['username_signup']
##            email = request.POST['email_signup']
##            password = request.POST['password_signup']
##            passwordConfirm = request.POST['password_confirm_signup']
##
##            country = request.POST['country_signup']
##            city = request.POST['city_signup']
##                        
##            passwordsMatch = (password == passwordConfirm)
##
##            if not passwordsMatch:
##                errorMsg = "passwords do not match"
##            if usernameExists(username):
##                errorMsg = "registered user with this username exists"
##            if emailExists(email):
##                errorMsg = "registered user with this email already exists"                   
##
##            #address and phone number validation
##            
##            
##            return render (request, "home.html", {})

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
        user = User.objects.get(email__iexact=email)
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
            return (user, "User is valid, active and authenticated")
        else:
            return (None, "Password valid, but account disabled")            
    elif user_email is not None:
        if user_email.is_active:
            return (user_email, "User is valid, active and authenticated")
        else:
            return (None, "Password valid, but account disabled")
    else:
        return (None, "Neither username nor email authentication worked. Password and/or username invalid")
        
        
