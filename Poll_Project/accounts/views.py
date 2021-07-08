from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import RegisterForm, LoginForm


def home(request):
    return HttpResponse("Here We go!")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.password == password:
                    return HttpResponse('Successful Login')
                else:
                    messages.info(request, 'Password Not Matching!')
                    return redirect('login')
            else:
                messages.info(request, 'No such username exists')
                return redirect('login')
        else:
            print('Invalid Form')
            return redirect('login')
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponse('Successful Logout')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already taken')
                    return redirect('register')
                else:
                    user = User.objects._create_user(username=username, password=password, email=email)
                    user.save()
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('register')
            return HttpResponse('Thanks for registering')
        else:
            print('Invalid Form')
            return redirect('register')
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)
