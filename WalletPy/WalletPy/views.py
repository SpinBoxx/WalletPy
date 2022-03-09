from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
import logging
import requests
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})

def homepage(request):
    test = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
    print(test.json())
    return render (request=request, template_name="homepage.html")

def dashboard(request):
    return render (request=request, template_name="dashboard/dashboard.html")
