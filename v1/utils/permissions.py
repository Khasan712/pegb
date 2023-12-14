from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    message = "You must be the staff of this website"

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_staff)
    

class IsCustomer(BasePermission):
    message = "You must be the customer of this website"

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and not request.user.is_staff)


class IsSuperUser(BasePermission):
    message = "You must be the superuser of this website"

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)
