from django.shortcuts import render

def home(request):
    return render(request, 'ardjson/intro.html')

def jsonView(request):
    return render(request, 'ardjson/json.html')

def humidityView(request):
    return render(request, 'ardjson/humidity.html')

def celsiusView(request):
    return render(request, 'ardjson/celsius.html')

def fahrenheitView(request):
    return render(request, 'ardjson/fahrenheit.html')
