from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("working")

def html(request):
    return render()