from django.shortcuts import render, redirect
from accounts.models import patient, doctor, nurse, medication, Department, room, appointment, payments, priscription
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms 

@login_required(login_url="login")
def patient_create(request):
    if request.method == 'POST':
        form = forms.Createpatient(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createpatient()

    return render(request, 'detail/patient_create.html', {'form':form})


@login_required(login_url="login")
def doctor_create(request):
    if request.method == 'POST':
        form = forms.Createdoctor(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('doc')
    else:
        form = forms.Createdoctor()

    return render(request, 'detail/doctor_create.html', {'form':form})


@login_required(login_url="login")
def nurse_create(request):
    if request.method == 'POST':
        form = forms.Createnurse(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createnurse()

    return render(request, 'detail/nurse_create.html', {'form':form})




@login_required(login_url="login")
def priscription_create(request):
    if request.method == 'POST':
        form = forms.Createpriscription(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createpriscription()

    return render(request, 'detail/priscription_create.html', {'form':form})




@login_required(login_url="login")
def medication_create(request):
    if request.method == 'POST':
        form = forms.Createmedication(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createmedication()

    return render(request, 'detail/medication_create.html', {'form':form})






@login_required(login_url="login")
def department_create(request):
    if request.method == 'POST':
        form = forms.Createdepartment(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createdepartment()

    return render(request, 'detail/department_create.html', {'form':form})





@login_required(login_url="login")
def appointment_create(request):
    if request.method == 'POST':
        form = forms.Createappointment(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createappointment()

    return render(request, 'detail/appointment_create.html', {'form':form})






@login_required(login_url="login")
def payments_create(request):
    if request.method == 'POST':
        form = forms.Createpyments(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createpyments()

    return render(request, 'detail/payments_create.html', {'form':form})



@login_required(login_url="login")
def room_create(request):
    if request.method == 'POST':
        form = forms.Createroom(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.Createroom()

    return render(request, 'detail/room_create.html', {'form':form})







def doctor_details(request):
    doctors = doctor.objects.all()
    return render(request, 'detail/doctor_details.html', {'doctors':doctors})


def nurse_details(request):
    nurses = nurse.objects.all()
    return render(request, 'detail/nurse_details.html', {'nurses':nurses})


def patient_details(request):
    patients = patient.objects.all()
    return render(request, 'detail/patient_details.html', {'patients':patients})