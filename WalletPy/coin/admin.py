from django.contrib import admin
from coin.models import Coin# Register your models here.


class CoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Coin, CoinAdmin)

