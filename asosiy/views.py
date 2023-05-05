from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('/loginview/')

def register(request):
    if request.method == "POST" and request.POST.get('p') == request.POST.get('cp'):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p'), )
        return redirect('/loginview/')
    return render(request, 'register.html')

def loginview(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('l'), password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')