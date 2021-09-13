from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# rendering an html site
def index(request):
    return render(request,"hello/index.html")

def adityaa(request):
    return HttpResponse("hello Adityaa :D")

def vivek(request):
    return HttpResponse("Hello vivek :D")

# creating a function says hello ,using url -

def hello(request,name=''):
    return render(request,"hello/hello.html",{
        "name":name.capitalize()
    })