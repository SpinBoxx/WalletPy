from pycoingecko import CoinGeckoAPI
from django.core import serializers
from coin.models import Coin

def get_available_coins_dashboard_data():
    cg = CoinGeckoAPI()
    coins = serializers.serialize("python",  Coin.objects.all())
    coin_data = []
    for coin in coins:
        cg_data = cg.get_coin_by_id(id=coin["fields"]["name"],localization=False,tickers=False,community_data=False,developer_data=False,sparkline=False)
        data = {
            "price_change_percentage_24h": cg_data["market_data"]["price_change_percentage_24h"],
            "current_price": cg_data["market_data"]["current_price"]["usd"],
            "thumb": cg_data["image"]["thumb"],
            "symbol":cg_data["symbol"]
        }
        coin_data.append(data)
    return coin_data