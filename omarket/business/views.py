from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/registration/signin/')
def home(request):
    return render(request, "business_dashboard.html", {})

@login_required(login_url='/registration/signin/')
def orders(request):
    return render(request, "business_orders.html", {})
