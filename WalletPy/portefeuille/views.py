from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    info = [
        {
            "name": 'Bitcoin',
            "concurrency": "BTC/EUR",
            "amount":2000,
            "imgUrl": "https://s2.coinmarketcap.com/static/img/coins/200x200/1.png",
            "possess": "6.7 BTC"
        },
        {
            "name": "Ethereum",
            "concurrency": "ETH/EUR",
            "amount": 1500,
            "imgUrl": "https://cryptonaute.fr/wp-content/uploads/2020/06/ethereum-logo.png",
            "possess": "6.7 ETH"
        },
        {
             "name": "Doge",
             "concurrency": "DOGE/EUR",
             "amount": 700,
             "imgUrl": "https://s2.coinmarketcap.com/static/img/coins/200x200/74.png",
             "possess": "1200.7 Doge"

        }
    ]
    context = {
        'information': info
    }
    return render (request, "portefeuille/index.html", context)
