from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
# Create your views here.
def loginUser(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            return redirect('/',{'user',user})  # Redirect to a home page
    else:
        form = AuthenticationForm()
    return render(req, 'user/login.html', {'form': form})
def registerUser(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(req, 'user/register.html', {'form': form})