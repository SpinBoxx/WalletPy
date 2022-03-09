from django.shortcuts import  render, redirect
import requests

def homepage(request):
    test = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
    print(test.json())
    return render (request=request, template_name="homepage.html")

def dashboard(request):
    return render (request=request, template_name="dashboard/dashboard.html")
