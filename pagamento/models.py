from django.db import models


# Create your models here.
class Pagamento(models.Model):
    idcliente = models.ForeignKey('clientes.Cliente',on_delete=models.CASCADE,)
    idcarrinho = models.ForeignKey('vendas.Carrinho', on_delete=models.CASCADE, )
    token = models.CharField(max_length=50)
    parcelas = models.IntegerField()
    v_parcelas = models.FloatField(max_length=100)
    v_total = models.FloatField(max_length=100)
    ent_rua = models.CharField(max_length=100)
    ent_numero = models.IntegerField()
    ent_complemento = models.CharField(max_length=100)
    ent_bairro = models.CharField(max_length=100)
    ent_cidade = models.CharField(max_length=100)
    ent_estado = models.CharField(max_length=100)
    ent_pais = models.CharField(max_length=100, default='Brasil')
    status = models.CharField(max_length=50)
