from django.conf.urls import include, url
from django.contrib import admin

from omarket.views import hello, pricing
from omarket.views import homepage


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'omarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', homepage),                      # home page   
    url(r'^hello/$', hello),                  # test hello page
    url(r'^admin/', include(admin.site.urls)),

    url('^registration/', include('registration.urls')),
    url('^address/', include('address.urls')),
    url('^business/', include('business.urls')),
    url('^pricing/', pricing),
]
