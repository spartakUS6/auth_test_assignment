from django.db import models
from access.models import Role  # твоя кастомная модель ролей

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)

    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    roles = models.ManyToManyField(Role, blank=True, related_name="users")

    def has_permission(self, perm_code: str) -> bool:
        if not self.is_active:
            return False
        return self.roles.filter(permissions__code=perm_code).exists()

    def __str__(self):
        return self.email
