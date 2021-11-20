from django.urls import path
from produtos.views import Produto
from . import views

urlpatterns = [
    path('', Produto.as_view(), name='produto'),
]