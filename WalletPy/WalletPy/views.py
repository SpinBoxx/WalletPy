from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  get_object_or_404, render, redirect
import requests
from datetime import date, timedelta
from coin.models import Coin

from coin.coin_service import get_available_coins_dashboard_data
from .forms import PriceSearchForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    """ test = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
    print(test.json()) """
    return render (request=request, template_name="homepage.html")

def dashboard(request):
    info = [
        {
            "name": 'Bitcoin',
            "concurrency": "BTC/EUR",
            "amount":2000,
            "imgUrl": "https://s2.coinmarketcap.com/static/img/coins/200x200/1.png"

        },
        {
            "name": "Ethereum",
            "concurrency": "ETH/EUR",
            "amount": 1500,
            "imgUrl": "https://cryptonaute.fr/wp-content/uploads/2020/06/ethereum-logo.png"
        },
        {
             "name": "Doge",
             "concurrency": "DOGE/EUR",
             "amount": 700,
             "imgUrl": "https://s2.coinmarketcap.com/static/img/coins/200x200/74.png"
        }
    ]
    coin_data = get_available_coins_dashboard_data(request.user)
    datetime_today = date.today()      # get current date
    date_today = str(datetime_today)    # convert datetime class to string
    date_10daysago = str(datetime_today - timedelta(days=10))     # get date of today -10 days
    api= 'https://api.coindesk.com/v1/bpi/historical/close.json?start=' + date_10daysago + '&end=' + date_today + '&index=[USD]'
    try:
        response = requests.get(api, timeout=2)    # get api response data from coindesk based on date range supplied by user
        response.raise_for_status()            # raise error if HTTP request returned an unsuccessful status code.
        prices = response.json()    #convert response to json format
        btc_price_range=prices.get("bpi")   # filter prices based on "bpi" values only
    except requests.exceptions.ConnectionError as errc:  #raise error if connection fails
        raise ConnectionError(errc)
    except requests.exceptions.Timeout as errt:   # raise error if the request gets timed out without receiving a single byte
        raise TimeoutError(errt)
    except requests.exceptions.HTTPError as err:   # raise a general error if the above named errors are not triggered
        raise SystemExit(err)
    date_from = None
    date_to = None
    wrong_input = None
    search_form= PriceSearchForm(request.POST or None)   #get post request from the front end
    if request.method == 'POST':
        if search_form.is_valid():   #Confirm if valid data was received from the form
            date_from = request.POST.get('date_from') #extract input 1 from submitted data
            date_to = request.POST.get('date_to')  #extract input 2 from submitted data
        else:
            raise Http400("Sorry, this did not work. Invalid input")
        api= 'https://api.coindesk.com/v1/bpi/historical/close.json?start=' + date_from + '&end=' + date_to + '&index=[USD]'  #use the 10days period obtained above to get default 10days value
        if date_to > date_from:     #confirm that input2 is greater than input 1
            try:
                response = requests.get(api, timeout=2) #get api response data from coindesk based on date range supplied by user
                response.raise_for_status()        #raise error if HTTP request returned an unsuccessful status code.
                response = requests.get(api) #get api response data from coindesk based on date range supplied by user
                prices = response.json() #convert response to json format
                btc_price_range=prices.get("bpi") #filter prices based on "bpi" values only
                from_date= date_from
                to_date= date_to
            except requests.exceptions.ConnectionError as errc:  #raise error if connection fails
                raise ConnectionError(errc)
            except requests.exceptions.Timeout as errt:     #raise error if the request gets timed out without receiving a single byte
                raise TimeoutError(errt)
            except requests.exceptions.HTTPError as err:       #raise a general error if the above named errors are not triggered
                raise SystemExit(err)
        else:
            wrong_input = 'Wrong date input selection: date from cant be greater than date to, please try again' #print out an error message if the user chooses a date that is greater than input1's date
    context = {
        'coin_data': coin_data,
        'price':btc_price_range,
        'search_form':search_form,
        'wrong_input' : wrong_input,
        'information': info
    }
    return render(request, 'dashboard/basedashbord.html', context)
  
def error_404(request, exception):
    return render(request,'error_404.html')

@login_required 
def favorite_add(request, id):
    current_user = request.user
    if current_user.favorite_coins.filter(id=id).exists():
        current_user.favorite_coins.remove(id)
    else:
        current_user.favorite_coins.add(id)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
