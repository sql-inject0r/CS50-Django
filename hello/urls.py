from django.urls import path 
from . import views

# creating urls for the app - 
urlpatterns = [
    path("",views.index,name='index'),
    path("adityaa",views.adityaa,name="adityaa"),
    path("vivek",views.vivek,name="viveek"),
    path("<str:name>",views.hello,name="hello")
]
