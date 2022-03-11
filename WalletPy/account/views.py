from django.shortcuts import render, redirect

def index(request):
    user = ''
    context = {user : request.user}
    return render(request, 'account.html', context)

def update_user(request):
    context = {}
    if request.method == 'POST':

        password = request.POST['new_password']
        username = request.POST['username']

        
        request.user.set_password(password)
        request.user.username = username
        request.user.save()

    return redirect('/profile', context)
        

