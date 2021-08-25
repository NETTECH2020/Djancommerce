from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index, name='home'),
    path('contactus/',views.contactus),
    path('test/',views.counter),
    path('registration/',views.registrationpage, name='registration'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutUser, name='logout')

]
admin.site.site_header = 'Shop Admin'



from django.urls import path 
from . import views



urlpatterns = [
    path('',views.index,name='home'),
    path('confirm', views.confirm),
    path('registration/',views.registrationpage,name='registartion'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('atm/',views.atmlogin, name= 'atm-page'),
    path('bluebox/',views.bluebox,name='bluebox'),
    path('Workschedule/',views.workSchedule,name='Workschedule'),
    path('Raise/',views.Raise,name='Raise'),

]
