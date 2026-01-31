from django.db import models


class AppPermission(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.code


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(
        AppPermission,
        blank=True,
        related_name="roles"
    )

    def __str__(self):
        return self.name