from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("migration/search", views.search, name='search'),
    path("migration/directing", views.directing, name='directing'),
    path("migration/translate", views.translate, name='translate')
]
