from django.urls import path
from pagamento.views import Pagamento
from . import views

urlpatterns = [
    path('', Pagamento.as_view(), name='pagamento'),
]