from django.urls import path
from .views import login,signup,administrator,farmer,home,profile,user,weather_api,weather_view

urlpatterns = [
    path('',login,name="login"),
    path('register/ ',signup,name="register"),
    path('administrator/',administrator,name="administrator"),
    path('farmer/',farmer,name="farmer"),
    path('home/',home,name="home"),
    path('profile/',profile,name="profile"),
    path('user/',user,name="user"),
    path('weather/', weather_view, name='weather'),
    path('weather-api/<str:area>/', weather_api, name='weather-api'),

]
