from rest_framework.permissions import BasePermission


# si no es usuario administrador solo podra tener acceso de lectura
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff