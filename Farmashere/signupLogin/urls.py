from django.contrib import admin
from django.urls import path
from .views import login,signup

urlpatterns = [
    path('login/',login,name=""),
    path('register/ ',signup,name="")
]
