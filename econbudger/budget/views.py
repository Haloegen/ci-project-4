from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_budget(request):
    return HttpResponse("I have made it")