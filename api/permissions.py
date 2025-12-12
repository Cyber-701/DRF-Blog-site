from rest_framework.permissions import BasePermission, SAFE_METHODS


class isAuthorOrReadOnly(BasePermission):
    def has_permissions(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False
            
    def has_object_permission(self, request, view, obj):
        if request.metho