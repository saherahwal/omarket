"""

Module: Business Views

Author: Saher Ahwal
Date:   March 2015

"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction

from business import forms as businessForms
from address.models import City, Country, Address
from address import utils as AddressUtils
from registration.models import UserProfile, SubscriptionType
from business.models import Business, BusinessType

#
# Localizable Strings
#
CITY_DOESNT_MATCH= "City Does not exist in country chosen."

@login_required(login_url='/registration/signin/')
def home(request):
    if (AddedBusinessEarlier( request.user )):
        return render(request, "business_dashboard.html", {})
    else:
        return render(request, "business_notaddedyet.html", {})

@login_required(login_url='/registration/signin/')
def orders(request):
    if (AddedBusinessEarlier( request.user )):
        return render(request, "business_orders.html", {})
    else:
        return render(request, "business_notaddedyet.html", {})        

@login_required(login_url='/registration/signin/')
def products(request):

    if (AddedBusinessEarlier( request.user )):
        #
        # Create unbounded Add Item form
        #
        addItemForm = businessForms.ItemAddForm()
        
        
        return render(request,
                      "business_products.html",
                      {'itemAddForm': addItemForm })
    else:
        return render(request, "business_notaddedyet.html", {})       

@login_required(login_url='/registration/signin/')
def addBusiness(request):

    #
    # if a business was added earlier, just show dashboard
    # currently, we only allow one business per user
    # under one subscription
    #
    if (AddedBusinessEarlier( request.user )):
        return render(request, "business_dashboard.html", {})
    
    #
    # Create unbounded Add-Business-Form
    #
    addBusinessForm = businessForms.BusinessForm()

    if request.method == 'POST':
        #
        # list of response errors
        #
        respErrors = []

        #
        # Create form instance to process data
        #
        addBusinessForm = businessForms.BusinessForm(request.POST, request.FILES)

        #
        # check form validity
        #
        if addBusinessForm.is_valid():
            name = addBusinessForm.cleaned_data['name']
            phone = addBusinessForm.cleaned_data['phone']
            image = addBusinessForm.cleaned_data['image']
            businessTypeId = addBusinessForm.cleaned_data['businessType']
            description = addBusinessForm.cleaned_data['description']
            countryId = addBusinessForm.cleaned_data['country']
            city = addBusinessForm.cleaned_data['city']
            zipCode = addBusinessForm.cleaned_data['zipcode']
            stateId = addBusinessForm.cleaned_data['state']
            streetAddress = addBusinessForm.cleaned_data['address']

            #
            # lookup country - guaranteed not fail
            # does city exist in the country?
            # NOTE: we guarantee that if city exists, it will be unique
            #
            countryObj = Country.objects.get( id=countryId )
            cityObjs = City.objects.filter( city_name=city,
                                            country=countryObj )

            if(len(cityObjs)==0):
                respErrors.append( CITY_DOESNT_MATCH )

            #
            # if errors exist - return
            #
            if len(respErrors) != 0:
                return render(request,
                              "business_addnew.html",
                              {'addBusinessForm': addBusinessForm,
                              'respErrors': respErrors })


            numCustomers = 0
            ## TODO: offers left should be implemented correctly 
            offersLeft = 0
            owner = None
            
            with transaction.atomic():

                #
                # retrieve user - auth check might be redundant
                #
                if request.user.is_authenticated():
                    owner = UserProfile.objects.get( id = request.user.id )

                #
                # retreive a business type
                #
                businessTypeObj = BusinessType.objects.get(id=businessTypeId)

                #
                # retreive address
                #
                countryObj = Country.objects.get(id=countryId)            
                cityObjs = City.objects.filter(city_name=city,
                                               country=countryObj)

                addressObj = Address.objects.create(street_address = streetAddress,
                                                    city = cityObjs[0],
                                                    zip_code = zipCode,
                                                    state = AddressUtils.getStateFromId(stateId))
                
                businessObj = Business.objects.create(name = name,
                                                      phone = phone,
                                                      img = image,
                                                      offers_left = offersLeft,
                                                      business_description = description,
                                                      num_customers = numCustomers,
                                                      owner = owner,
                                                      business_type = businessTypeObj)

                businessObj.addresses.add( addressObj)
                businessObj.save()
            #
            # at this point we succeeded
            #            
            return render(request,
                          "business_dashboard.html",
                          {'addBusinessForm': addBusinessForm,
                           'respErrors': respErrors })            
            
        else:
            #
            # form is invalid
            #
            return render(request,
                          "business_addnew.html",
                          {'addBusinessForm': addBusinessForm,
                           'respErrors': respErrors })
    else:        
        #
        # Non-POST requests 
        #
        return render(request,
                      "business_addnew.html",
                      {'addBusinessForm': addBusinessForm})    
        

@login_required(login_url='/registration/signin/')
def addItem(request):
    
    #
    # Create unbounded Add Item form
    #
    addItemForm = businessForms.ItemAddForm()
    
    if request.method == 'POST':
        #
        # list for response errors
        #
        respErrors = []
    
        #
        # Create form instance to process data
        #
        addItemForm = businessForms.ItemAddForm(request.POST)

        #
        # check form validity
        #
        if addItemForm.is_valid():
            title = loginForm.cleaned_data['title']
            productType = loginForm.cleaned_data['productType']
            vendor = loginForm.cleaned_data['vendor']
            description = loginForm.cleaned_data['description']
            chargeTaxes = loginForm.cleaned_data['chargeTaxes']
            shippingRequired = loginForm.cleaned_data['shippingRequired']
            tags = loginForm.cleaned_data['tags']
            currency = loginForm.cleaned_data['currency']
            shoppingCategory = loginForm.cleaned_data['shoppingCategory']
            newCategory = loginForm.cleaned_data['newCategory']
            image = loginForm.cleaned_data['image']
            
##            with transaction.atomic():
##                Vendor.objects.get_or_create( name = vendor )
##                
##                if(len(newCategory) > 0):
##                   shoppingCategory =  ShoppingCategory( category_name = newCategory )
                
           

        else:
            #
            # form is invalid
            #
            return render(request,
                          "business_products.html",
                          {'itemAddForm': addItemForm})
    else:
        
        #
        # Non-POST requests 
        #
        return render(request,
                      "business_products.html",
                      {'itemAddForm': addItemForm})


#
# Helper functions
#
def AddedBusinessEarlier( currentUser ):
    """ returns true if the current user (request.user) added business, false otherwise """
    if currentUser.is_authenticated():

        #
        # get user object
        #
        userProfileObj = UserProfile.objects.get( id = currentUser.id )

        #
        # get business query set for the user - currently we support only one
        # business to each owner (user)
        #
        businessQuerySet = Business.objects.filter( owner = userProfileObj)
        
        return (len(businessQuerySet) != 0) 
    else:
        return False
    
    

            
        

    

