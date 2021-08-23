from Sino.models import SA
from django.contrib import admin


class SAAdmin(admin.ModelAdmin):
    
    list_display = ('Firstname', 'Lastname', 'Email','PhoneNo')


admin.site.register(SA,SAAdmin)

