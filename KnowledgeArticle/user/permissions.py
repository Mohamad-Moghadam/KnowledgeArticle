from rest_framework.permissions import BasePermission
from article.models import Article


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name = "Admin").exists()

class IsEditorUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.groups.filter(name="Editor").exists() and request.user == obj.creator
        return request.user.groups.filter(name="Editor").exists()

class IsAdminOrEditorUser(BasePermission):
    def has_permission(self, request, view):
        return IsAdminUser().has_permission(request, view) or request.user.groups.filter(name="Editor").exists()

    def has_object_permission(self, request, view, obj):
        if IsAdminUser().has_permission(request, view):
            return True
        return IsEditorUser().has_object_permission(request, view, obj)


class IsViewerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name = "Viewer").exists()