from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm

def signin(request):
    form = LoginForm()
    context={
        'form': form
        }   
    return render(request, 'user/signin.html',context=context)  # Render template instead of redirect
def signup(request):
    form = RegisterForm()  
    return render(request, 'user/signup.html',{'form': form})  # Same fix for signup
def signout(request):
    logout(request)
    return redirect('/')  # Redirect works correctly here
