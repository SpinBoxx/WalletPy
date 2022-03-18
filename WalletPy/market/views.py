from django.shortcuts import render
from coin.coin_service import get_available_coins_dashboard_data

# Create your views here.
def index(request):
    coin_data = get_available_coins_dashboard_data(request.user)

    context = {
        'coin_data' : coin_data
    }


    return render (request, "market/index.html", context)
