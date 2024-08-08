"""
URL configuration for user_Money project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Customer_Registration, name='registration'),
    path('login',views.login, name='registration'),
    path('Amount-Deposite', views.opetion_provide, name='index'),

    # this urls call is amount enter
    path('Amount',views.get, name='Enter-Amount'),
    # this urls call amount data send
    path('enter', views.Amount_view, name='Enter-Amount'),
    
    path('draw', views.Draw, name='Amount-withdraw'),
    path('cashback', views.Cash_Back, name='Amount-withdraw'),
    path('admin/', admin.site.urls),
]