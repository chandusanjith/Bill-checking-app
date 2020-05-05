"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import LoginLoad, login, MainLoad, LoadDate, AdminsLoad, LoadData, AddDataLoad, AddData, ChangeStatus

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', LoginLoad),
    path('login/', login),
    path('main/', MainLoad),
    path('loaddate/', LoadDate),
    path('admins/', AdminsLoad),
    path('LoadData/', LoadData),
    path('adddata/', AddDataLoad),
    path('adddatatomodel/', AddData),
    path('changestatus/<uid>/<month>/', ChangeStatus)
]