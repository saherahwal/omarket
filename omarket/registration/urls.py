from django.conf.urls import include, url
from django.contrib import admin

from registration.views import home, signin, signup, signout

urlpatterns = [
    # Examples:
    # url(r'^$', 'omarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^home/$', home),
    url(r'^signin/$', signin),
    url(r'^signup/$', signup),
    url(r'^signout/$', signout)
    
    
 
]