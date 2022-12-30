from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def home_page(request):
    return render (request, 'base.html')


@login_required(login_url="login")
def doctor_home(request):
    return render (request, 'doctor_home.html')


@login_required(login_url="login")
def nurse_home(request):
    return render (request, 'nurse_home.html')
