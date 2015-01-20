from django.contrib import admin
from address.models import *

# Register your models here.

admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
