from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator
from django.contrib import messages

def index(request):
    user = ''
    context = {user : request.user}
    return render(request, 'account.html', context)

def update(request):
    context = {}
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['new_password']
        validators = [MinimumLengthValidator, CommonPasswordValidator]

        if password != "":
            try:
                for validator in validators:
                    validator().validate(password)
                request.user.set_password(password)    
                messages.success(request, 'Mot de passe changé')
            except ValidationError as error:
                messages.error(request, error)
                

        if request.user.username != username and username != "":
            request.user.username = username
            messages.success(request, 'Votre pseudo à été mis à jour')

        request.user.save()
    	
        user = authenticate(username=username, password=password)
        login(request, user)

    return redirect('/profile', context)
        

