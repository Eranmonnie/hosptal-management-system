from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse


def patient(request):
    return HttpResponse('hii')

def doctor(request):
    return HttpResponse('hii')

def nurse(request):
    return HttpResponse('hii')