from django.contrib import admin
from .models import Produto, Categoria, RelacaoProduto, ProdCategoria, Desconto, ProdCor, Cor, ProdTamanho, Tamanho
# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(RelacaoProduto)
admin.site.register(ProdCategoria)
admin.site.register(Desconto)
admin.site.register(ProdCor)
admin.site.register(Cor)
admin.site.register(ProdTamanho)
admin.site.register(Tamanho)