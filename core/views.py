from os import stat
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from core.serializers import *
from core.models import *

# Create your views here.
class ProdutoViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def create(self, request, *args, **kwargs):
        user = self.request.user
        query = User.objects.get(id=user.id)
        if query:
            return JsonResponse(data = {'error':'Usuario ja pertence ao banco'}, status = status.HTTP_409_CONFLICT)
        return super().create(request, *args, **kwargs)