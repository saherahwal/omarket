from django.conf.urls import include, url
from django.contrib import admin

from address.views import cities, phoneCode

urlpatterns = [
    # Examples:
    # url(r'^$', 'omarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),  
    
    url(r'^cities/$', cities),
    url(r'^phoneCode/$', phoneCode),
    
]
