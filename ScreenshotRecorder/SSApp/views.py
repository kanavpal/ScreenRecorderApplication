from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.conf import settings
import os


def home(request):
    return render(request,'home.html')


def signup(request):
    # if not request.user.is_anonymous:
    #     return redirect("/signup")
    
    if request.method=="POST":

        User = get_user_model()
        users = User.objects.all()
        user_list=[]
        email_list=[]
        for i in users:
            user_list.append(i.username)
            email_list.append(i.email)

        acc_type=str(request.POST.get('IN_OC'))

        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if email in email_list:
            messages.error(request, 'Email already signed up. Head to login page.')
            return render(request,'signup.html')
        if name in user_list:
            messages.error(request, 'Username already exists. Get another username')
            return render(request,'signup.html')
        
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()

        npath = os.path.join('../ScreenshotRecorder/static/screenrecordings', name)

        os.mkdir(npath)

        messages.success(request, f'Your account was created. Your username is {name}. Head to login page')
        
    return render(request,'signup.html')