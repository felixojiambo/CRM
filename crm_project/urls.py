from django.contrib import admin
from django.urls import path
from crm_project import views
urlpatterns = [
    path('', views.home,name=home),
]
