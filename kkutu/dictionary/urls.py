from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('database/', views.database, name="database"),
    path('wordsheet/', views.wordsheet, name="wordsheet"),
    path('main/', views.main, name="main"),
    path('wordsheet/backletter/', views.backletter, name="backletter"),
    path('wordsheet/frontletter/', views.frontletter, name="frontletter"),
    path('wordsheet/attack/', views.attack, name="attack"),
    path('wordsheet/onetime/', views.onetime, name="onetime"),
    path('wordsheet/threeletter/', views.threeletter, name="threeletter"),
    path('wordsheet/wordbattle/', views.wordbattle, name="wordbattle"),
]
