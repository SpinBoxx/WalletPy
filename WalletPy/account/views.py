from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required


from coin.models import Fiat

@login_required
def index(request):
    fiat = Fiat.objects.all()
    user = ''
    context = {"user" : request.user, "available_fiat": fiat}
    return render(request, 'account.html', context)

@login_required
def update(request):
    context = {}

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['new_password']

        pref_fiat = str(request.POST['pref_fiat'])
        validators = [MinimumLengthValidator, CommonPasswordValidator]

        if password != "":
            try:
                for validator in validators:
                    validator().validate(password)
                request.user.set_password(password)
                messages.success(request, 'Mot de passe changé')
            except ValidationError as error:
                messages.error(request, error)



        if str(request.user.preferred_currency.id) != pref_fiat and pref_fiat != "":
            request.user.preferred_currency = Fiat.objects.get(id=pref_fiat)
            messages.success(request, 'Monnaie de conversion modifié')

        if request.user.username != username and username != "":
            request.user.username = username
            messages.success(request, 'Votre pseudo à été mis à jour')

        request.user.save()

        user = authenticate(username=username, password=password)
        login(request, user)

    return redirect('/profile', context)
