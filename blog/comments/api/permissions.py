from rest_framework.permissions import BasePermission

from comments.models import Comment

# si no s propietario del post solo podra leer y crear comentarios
class IsOwnerOrReadAndCreatedOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # obtiene el id del comentario
            id_comment = view.kwargs['pk']
            # obtiene los datos del comentario
            comment = Comment.objects.get(pk=id_comment)
            
            # obtiene el id del usuario que esta ejecutando la petición
            id_user = request.user.pk
            
            # obtiene el id del usuario que realizó el comentario
            id_user_comment = comment.user_id
            
            # el usuario que está haciendo la petición es el creador del comentario
            if id_user == id_user_comment:
                return True
            
            return False