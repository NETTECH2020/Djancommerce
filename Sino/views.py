from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def counter(request):
    text1=request.GET['text']
    amount_of_words=text1
    passwo=request.GET['password']
    passwor=passwo  
    
    return render(request,'test.html',{'amount':amount_of_words,'pass':passwor},)

def registrationpage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration.html', context)

def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'INCORRECT USERNAME OR PASSWORD! TRY AGAIN')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
