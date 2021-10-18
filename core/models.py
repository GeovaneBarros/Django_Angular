from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Produto(models.Model):
    marca = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self) -> str:
        return (f'{self.nome} {self.marca} {self.preco}')

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'