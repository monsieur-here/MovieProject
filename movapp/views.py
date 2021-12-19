from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import userLogin
# Create your views here.

def register(request):
    userlogin = userLogin.objects.all()

    if request.method == 'POST':
        username = request.POST[username]
        password = request.POST[password]

        if " " not in password:
            if User.objects.filter(username=username).exists:
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            else:
                user = User.objects.filter(username=username, password=password)
                user.save()
                return redirect('register')
        else:
            messages.info(request, 'Invalid Password')
            return redirect('/')
    else:
        return render(request, 'register.html', {'userlogin': userlogin})