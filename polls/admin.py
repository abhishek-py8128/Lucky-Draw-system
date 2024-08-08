from typing import Any
from django.contrib import admin
# from django.db.models.query import QuerySet
# from django.http.request import HttpRequest
from polls.models import Registration, Customer, Win, Admins

# Register your models here.

class AdminRegistration(admin.ModelAdmin) :
    list_display = ['id','name','mail', 'pswd'] 

class AdminCustomer(admin.ModelAdmin) :
    list_display = ['id', 'name', 'amount']

class AdminWin(admin.ModelAdmin) :
    list_display = ['id', 'Date', 'name', 'amount']

class AdminAdmins(admin.ModelAdmin) :
    list_display = ['id', 'name', 'mail']
    
    def get_all_permissions(obj=None) :
        pass    
    
admin.site.register(Registration, AdminRegistration)          
admin.site.register(Customer, AdminCustomer)
admin.site.register(Win, AdminWin)
admin.site.register(Admins, AdminAdmins)