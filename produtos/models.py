from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    valor = models.FloatField(max_length=100)
    descricao = models.CharField(max_length=5000)
    p_desconto = models.FloatField(max_length=100)
    foto = models.ImageField(upload_to='fotos/produtos')
    v_total = models.FloatField(max_length=100)
    categoria = models.CharField(max_length=100)
    em_oferta = models.BooleanField(default=True)

class ProdCor(models.Model):
    idproduto = models.ForeignKey('Produto', on_delete=models.CASCADE, )
    idcores = models.ForeignKey('Cor', on_delete=models.CASCADE, )

class Cor(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/cores')
    quantidade = models.IntegerField(default=0)

class ProdTamanho(models.Model):
    idproduto = models.ForeignKey('Produto', on_delete=models.CASCADE, )
    idtamanhos = models.ForeignKey('Tamanho', on_delete=models.CASCADE, )

class Tamanho(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/tamanhos')
    quantidade = models.IntegerField(default=0)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=5000)

class ProdCategoria(models.Model):
    idproduto = models.ForeignKey('Produto', on_delete=models.CASCADE, )
    idcategoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, )


class RelacaoProduto(models.Model):
    idproduto1 = models.IntegerField(default=0)
    idproduto2 = models.IntegerField(default=0)
    iddesconto = models.ForeignKey('Desconto', on_delete=models.CASCADE, )

class Desconto(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    valor = models.FloatField(max_length=100)
    status = models.CharField(max_length=50)