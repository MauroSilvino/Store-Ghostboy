from django.urls import path
from clientes.views import Cliente
from . import views

urlpatterns = [
    path('', Cliente.as_view(), name='cliente'),
]