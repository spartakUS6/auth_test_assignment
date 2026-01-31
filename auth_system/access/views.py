from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from core.permissions import require_permission
from users.models import User
from access.models import Role, AppPermission


@require_permission("admin.manage_roles")
@require_http_methods(["POST"])
def assign_role(request):
    user_id = request.POST.get("user_id")
    role_name = request.POST.get("role")

    user = User.objects.get(id=user_id)
    role = Role.objects.get(name=role_name)

    user.roles.add(role)
    return JsonResponse({"detail": "Role assigned"})


@require_permission("admin.manage_permissions")
@require_http_methods(["POST"])
def add_permission_to_role(request):
    role = Role.objects.get(name=request.POST["role"])
    perm, _ = AppPermission.objects.get_or_create(code=request.POST["permission"])
    role.permissions.add(perm)
    return JsonResponse({"detail": "Permission added"})
