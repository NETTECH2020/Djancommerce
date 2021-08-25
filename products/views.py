from django.shortcuts import render


def products(request):
    
    return render(request,'products.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
import datetime 
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
# from openpyxl.styles import Font


# @unauthenticated_user

@login_required(login_url='login')
@admin_only
def index(request):
    products=Product.objects.all()
    dat=datetime.datetime.now()
    usr=request.POST.get('userna')
    pword=request.POST.get('passwo')
    pf=request.POST.get('pw1')
    params = {'products':products, 'date':dat, 'name':usr, 'pass':pf}
    return render(request,'index.html',params)

@login_required(login_url='login')
def atmlogin(request):
    return render(request,'ATM.html')

@login_required(login_url='login')
def bluebox(request):
    return render(request,"Bluebox.html")

@login_required(login_url='login')
def workSchedule(request):
    return render(request, 'Workschedule.html')

@login_required(login_url='login')
def Raise(request):
    return render(request,'Raise.html') 
    

    # engine =pyttsx3.init()
    # p = engine.say('HELLO SIR')
    # hel=engine.runAndWait()



    
    

def confirm(request):
    pword=request.POST.get('passwo')
    pf=request.POST.get('pw1')
    usr=request.POST.get('userna')
    dat=datetime.datetime.now()
    if pword==pf:
        params = {'date':dat, 'name':usr, 'pass':pword}
        return render(request,'confirm.html',params)
    else:
        return HttpResponse ('''ERROR-404-NOT-FOUND''') 
# Create your views here.
# wb = Workbook()
# ws = wb.active
# ws.title ="New Data"
# headings = ['Name'] + list(products.keys())
# ws.append(headings)
# for person in products:
#     grades = list(products[person].values())
# ws.append([person] + grades)
# for col in range(2,len(products["Joe"])+2):
#     char = get_column_letter(col)
#     ws[char+"7"] = f"=SUM({char+'2'}:{char+'6'})/{len(products)}"
# wb.save("NewAutom.xlsx")


def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'INCORRECT USERNAME OR PASSWORD! TRY AGAIN')

            
    context = {}
    return render(request, 'login.html', context)


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

def logoutUser(request):
    logout(request)
    return redirect('login')


# Create your views here.
