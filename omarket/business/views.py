from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction

from business import forms as businessForms


@login_required(login_url='/registration/signin/')
def home(request):
    return render(request, "business_dashboard.html", {})

@login_required(login_url='/registration/signin/')
def orders(request):
    return render(request, "business_orders.html", {})

@login_required(login_url='/registration/signin/')
def products(request):

    #
    # Create unbounded Add Item form
    #
    addItemForm = businessForms.ItemAddForm()
    
    
    return render(request,
                  "business_products.html",
                  {'itemAddForm': addItemForm })

def addBusiness(request):
    pass


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
            
            
        

    

