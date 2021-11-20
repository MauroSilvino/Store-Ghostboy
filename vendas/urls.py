from django.urls import path
from vendas.views import Venda
from . import views

urlpatterns = [
    path('', Venda.as_view(), name='venda'),
]