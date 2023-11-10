from django.shortcuts import render
from rest_framework import viewsets

def home(request):
    return render(request, 'ardjson/intro.html')

def jsonView(request):
    return render(request, 'ardjson/json.html')