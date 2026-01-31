from django.urls import path
from .views import assign_role, add_permission_to_role

urlpatterns = [
    path("assign-role/", assign_role),
    path("add-permission/", add_permission_to_role),
]
