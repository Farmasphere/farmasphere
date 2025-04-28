from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
import requests
from django.http import JsonResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # or dashboard or wherever
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request,'signupLogin/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        # Create new user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, 'Account created successfully!')
        return redirect('login')
    return render(request,'signupLogin/signup.html')

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def administrator(request):
    return render(request,'dashboard/admin-dashboard.html')

def farmer(request):
    return render(request,'dashboard/farmer-dashboard.html')

def user(request):
    return render(request,'user-management.html')

def fetch_weather_data(city):
    api_key = 'Yd4693228a24cbd258bd1bb096e4514e2'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

# View to render the weather page
def weather_view(request):
    return render(request, 'weather.html')

# API endpoint to fetch weather for a specific area
def weather_api(request, area):
    # Fetch weather for the given area
    weather_data = fetch_weather_data(area)
    
    # Structure the data to send back as JSON
    data = {
        'city': weather_data.get('name'),
        'temperature': weather_data['main']['temp'],
        'humidity': weather_data['main']['humidity'],
        'conditions': weather_data['weather'][0]['description'],
    }
    
    return JsonResponse(data)
