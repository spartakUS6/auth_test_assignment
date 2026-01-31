from django.http import JsonResponse
from core.permissions import require_permission


@require_permission("reports.view")
def reports(request):
    return JsonResponse([
        {"id": 1, "name": "Sales report"},
        {"id": 2, "name": "Finance report"},
    ], safe=False)
