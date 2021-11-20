from django.db import models

# Create your models here.
class Cliente(models.Model):
    nomecompleto = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.IntegerField()
    cpf = models.IntegerField()
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, default='Brasil')
    foto = models.ImageField(upload_to='fotos/clientes')
    criado_em = models.DateTimeField(auto_now_add=True)
