from rest_framework.permissions import BasePermission
from .models import RoleChoices

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.role == RoleChoices.USER
        )
    
