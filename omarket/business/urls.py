from django.conf.urls import include, url
from django.contrib import admin

from business.views import home
from business.views import orders
from business.views import products
from business.views import addItem
from business.views import addBusiness


urlpatterns = [
    # Examples:
    # url(r'^$', 'omarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),  
    
    url(r'^home/$', home),
    url(r'^orders/$', orders),    
    url(r'^products/$', products),

    # products operations
    url(r'^products/addItem$', addItem),
    
    
    
]
