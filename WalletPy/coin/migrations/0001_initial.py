# Generated by Django 4.0.3 on 2022-03-18 08:43

from django.db import migrations, models

DEFAULT_FIAT = (
    ('american dollar','usd', '$'),
    ('euro','eur', '€')
)

def add_fiat(apps, schema_editor):
    Fiat = apps.get_model('coin', 'Fiat')
    for name,short_name, symbol in DEFAULT_FIAT:
        print(short_name)
        fiat = Fiat(name=name,symbol=symbol,short_name=short_name)
        fiat.save()

DEFAULT_COINS = (
    ('ethereum', 'ETH'),
    ('bitcoin', 'BTC'),
    ('litecoin', 'LTC'),
    ('chainlink', 'LINK'),
    ('ripple', 'XRP'),
    ('solana', 'SOL'),
    ('cardano', 'ADA'),
    ('polkadot', 'DOT')
)

def add_coin(apps, schema_editor):
    Coin = apps.get_model('coin', 'Coin')
    for name, symbol in DEFAULT_COINS:
        coin = Coin(name=name,symbol=symbol)
        coin.save()
            
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Fiat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=3)),
                ('short_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RunPython(add_coin),
        migrations.RunPython(add_fiat),
    ]