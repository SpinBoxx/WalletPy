from django.shortcuts import render
from django.http import HttpResponse
import csv
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse

# Create your views here.
def index(request):
        return render (request, "portefeuille/index.html")

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
