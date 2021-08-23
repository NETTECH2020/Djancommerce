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
