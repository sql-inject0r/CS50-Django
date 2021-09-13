from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#global variable - 
tasks = ["homework","lunch","sat prep"]

def index(request):
    return render(request,"tasks/index.html",{
        "tasks": tasks
    })


