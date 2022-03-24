from django.shortcuts import render
from django.http import HttpResponse
import csv
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse

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

def exportWalletCsv(request):
    post_data = json.loads(request.body.decode("utf-8"))

    header = ['Compte', 'Montant', 'Devise']
    data = [
        [post_data.get("address"), post_data.get("amount"), 'ETH'],
    ]
    current_user = request.user
    src = '/static/export_wallet/'
    filename = 'export_wallet_' + str(current_user.id) + '.csv'
    path =  src + filename
    f = open('.' +path, 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
    f.close()

    return JsonResponse({'filename': filename, 'path' : path })
