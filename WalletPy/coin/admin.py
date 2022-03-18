from django.contrib import admin
from coin.models import Coin, Fiat
# Register your models here.

class CoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Coin, CoinAdmin)

class FiatAdmin(admin.ModelAdmin):
    list_display = ('name','short_name', 'symbol')

admin.site.register(Fiat, FiatAdmin)