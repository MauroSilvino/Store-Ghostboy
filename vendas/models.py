from django.db import models

# Create your models here.
class Pedido(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    idcliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, )
    idpagamento = models.ForeignKey('pagamento.Pagamento', on_delete=models.CASCADE, )

class ProdPedido(models.Model):
    idproduto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, )
    idpedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, )

class Carrinho(models.Model):
    idcliente = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, )
    v_total = models.FloatField(max_length=100)
    d_total = models.FloatField(max_length=100)
    v_final = models.FloatField(max_length=100)
    modificado_em = models.DateTimeField(auto_now=True)

class ProdCarrinho(models.Model):
    idproduto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, )
    idcarrinho = models.ForeignKey('Carrinho', on_delete=models.CASCADE, )