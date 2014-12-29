from django.shortcuts import render
from django.http import HttpResponse
import json

from address.models import City, Country

# Create your views here.

#
# cities get by country
#
def cities(request):
    cities = []
    data = {}
    if request.is_ajax():
        country_id = request.POST.get('value')
        country_name = request.POST.get('text')       
        cities = City.objects.filter(country_id = int(country_id))        
    
    for c in cities:
        data[c.id] = c.city_name 

    jsonData = json.dumps(data)
    return HttpResponse(jsonData ,content_type="application/json")    
                   

#
# country code by country
#
def phoneCode(request):
    data = {}
    if request.is_ajax():
        country_id = request.POST.get('value')
        country_name = request.POST.get('text')

        country = Country.objects.get(id = country_id)
        data['phone_code'] = country.phone_code

    jsonData = json.dumps(data)
    return HttpResponse(jsonData, content_type="application/json")
