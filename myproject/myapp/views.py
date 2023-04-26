from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    path = request.path
    return HttpResponse(path, content_type = 'text/html' , charset="utf-8")