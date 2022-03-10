from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def register_request(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.") 
    else:
        form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})