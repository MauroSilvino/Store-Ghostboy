from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Cliente(TemplateView):
    def get(self, request):
        return render(request, 'clientes/cliente.html')