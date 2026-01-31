from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect



urlpatterns = [
    path("users/", include("users.urls")),
]