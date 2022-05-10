from unicodedata import name
from django.contrib import admin
from django.urls import path
from App import views
urlpatterns = [
    path("",views.index, name='App'),
    # path("about",views.about, name='about'),
    # path("services",views.services  , name='services'),
    path("contact",views.contact  , name='contact ')

]
