from django.urls import path
from users import views
from .views import login, logout, me, soft_delete

urlpatterns = [
    path("register/", views.register),
    path("login/", login),
    path("logout/", logout),
    path("me/", me),
    path("delete/", soft_delete),
]
