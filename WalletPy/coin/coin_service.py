from pycoingecko import CoinGeckoAPI
from django.core import serializers
from coin.models import Coin
import html
from django.core.exceptions import ObjectDoesNotExist

cg = CoinGeckoAPI()
def get_available_coins_dashboard_data(current_user):
    coin_data = {}
    headers = {"Content-type": "application/json"}
    markets = cg.get_coins_markets(current_user.preferred_currency.short_name)
    for coin in markets:
        try:
            local_coin = Coin.objects.get(name=coin["id"])
        except ObjectDoesNotExist:
            local_coin = None
        
        if not local_coin :
            continue
        
        data = {
            "internal_id": local_coin.id,
            "price_change_percentage_24h": coin["price_change_percentage_24h"],
            "current_price": coin["current_price"],
            "description": coin["name"],
            "thumb": coin["image"].replace("large","thumb"),
            "symbol":coin["symbol"],
            "is_favorite": False,
            "name": coin["id"]
        }
        if current_user.is_authenticated:
            data["is_favorite"]= current_user.favorite_coins.filter(id=local_coin.id).exists()
        coin_data[coin["id"]] = data
    return coin_data

def get_coin_simple_data(name:str):
    coin_data = {}
    cg_data = cg.get_coin_by_id(id=name,localization=False,tickers=False,community_data=False,developer_data=False,sparkline=False)
    name = {
            "price_change_percentage_24h": cg_data["market_data"]["price_change_percentage_24h"],
            "current_price": cg_data["market_data"]["current_price"]["usd"],
            "description": html.escape(cg_data["description"]["en"]),
            "thumb": cg_data["image"]["thumb"],
            "symbol":cg_data["symbol"],
    }
    return coin_data
