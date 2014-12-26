from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
            # authenticate
            #
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #redirect to success page - apply login
                else:
                    respErrors.append("user account not active")                    
                    return render(request, "login.html", {'loginForm': loginForm}) 
            else:
                respErrors.append("username or password incorrect")             
                            
        return render(request, "login.html", {'loginForm': loginForm, 'respErrors': respErrors }) 
        
    elif request.method == 'GET':
        loginForm = regForms.LoginForm()
        return render(request, "login.html", {'loginForm': loginForm})
    else:
        loginForm = regForms.LoginForm()
        return render(request, "login.html", {'loginForm': loginForm})
    
    

def signup(request):
    if request.method == 'POST':
        errorMsg = "success"
        if 'username_signup' in request.POST and \
           'email_signup' in request.POST and \
           'password_signup' in request.POST and \
           'password_confirm_signup' in request.POST:
            
            username = request.POST['username_signup']
            email = request.POST['email_signup']
            password = request.POST['password_signup']
            passwordConfirm = request.POST['password_confirm_signup']

            country = request.POST['country_signup']
            city = request.POST['city_signup']
                        
            passwordsMatch = (password == passwordConfirm)

            if not passwordsMatch:
                errorMsg = "passwords do not match"
            if usernameExists(username):
                errorMsg = "registered user with this username exists"
            if emailExists(email):
                errorMsg = "registered user with this email already exists"                   

            #address and phone number validation
            
            
            return render (request, "home.html", {})

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
   

def omarketAuth( username, passwd ):
    user = authenticate(username=username, password=passwd)
    if user is not None:
        # password is valid
        if user.is_active:
            print("User is valid, active and authenticated")
        else:
            print("Password valid, but account disabled")            
    else:
        # auth system was unable to verify username and password
        print("The username and password is incorrect")
