from pycoingecko import CoinGeckoAPI
from django.core import serializers
from coin.models import Coin
import html

cg = CoinGeckoAPI()
def get_available_coins_dashboard_data(current_user):
    coins = serializers.serialize("python",  Coin.objects.all())
    coin_data = {}
    headers = {"Content-type": "application/json"}
    for coin in coins:
        cg_data = cg.get_coin_by_id(id=coin["fields"]["name"],localization=False,tickers=False,community_data=False,developer_data=False,sparkline=False, headers = headers)
        data = {
            "internal_id": coin["pk"],
            "price_change_percentage_24h": cg_data["market_data"]["price_change_percentage_24h"],
            "current_price": cg_data["market_data"]["current_price"]["usd"],
            "description": html.escape(cg_data["description"]["en"]),
            "thumb": cg_data["image"]["thumb"],
            "symbol":cg_data["symbol"],
            "is_favorite": False,
            "name": cg_data["id"]
        }
        if current_user.is_authenticated:
            data["is_favorite"]= current_user.favorite_coins.filter(id=coin["pk"]).exists()
        coin_data[coin["fields"]["name"]] = data
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
