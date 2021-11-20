from django.contrib import admin
from .models import Carrinho, ProdPedido, Pedido, ProdCarrinho
# Register your models here.
admin.site.register(Carrinho)
admin.site.register(ProdPedido)
admin.site.register(Pedido)
admin.site.register(ProdCarrinho)