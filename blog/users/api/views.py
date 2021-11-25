from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.api.serializers import (
    UserRegisterSerializer,
    UserSerializer,
    UserUpdateSerializer
)


# permite registrar un usuario
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# realiza un override de User
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    # permite obtener los datos del usuario logueado
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    # permite actualizar los datos del usuario
    def put(self, request):
        # obtiene los datos del usuario que está realizando la petición
        user = User.objects.get(id=request.user.id)
        # le pasa los datos que tiene el user y los nuevos datos que se ingresen
        serializer = UserUpdateSerializer(user, request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        