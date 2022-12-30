from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout
from detail import forms 
from django.contrib.auth.models import Group



def register (request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return render('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user=user.save()

                auth.login(request,user)
                
                my_patient_group = Group.objects.get_or_create(name='PATIENT')
                my_patient_group[0].user_set.add(user)
                return redirect('login')

        else:
            messages.info(request, 'passwords dont match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def register_doctor (request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return render('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user=user.save()

                auth.login(request,user)

                my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
                my_doctor_group[0].user_set.add(user)
                return redirect('login')

        else:
            messages.info(request, 'passwords dont match')
            return redirect('register')

    else:
        return render(request, 'accounts/register_doctor.html')


def register_nurse (request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return render('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user=user.save()

                auth.login(request,user)

                my_nurse_group = Group.objects.get_or_create(name='NURSE')
                my_nurse_group[0].user_set.add(user)
                
                return redirect('login')

        else:
            messages.info(request, 'passwords dont match')
            return redirect('register')

    else:
        return render(request, 'accounts/register_nurse.html')


def is_nurse(user):
    return user.groups.filter(name='NURSE').exists()
    
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
    
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

        
def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
           if is_doctor(request.user):
         
                auth.login(request,user)
                return redirect('doc')

           elif is_nurse(request.user):

                auth.login(request,user)
                return redirect('nurse')

           elif "next" in request.POST:
                return redirect(request.POST.get('next'))
            
           else:
                auth.login(request,user)
                return redirect('home')
           
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')






def login_doctor(request): 
        return render(request, 'accounts/login_doctor.html')


def login_nurse(request):
        return render(request, 'accounts/login_nurse.html')

    


def logout_views(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

