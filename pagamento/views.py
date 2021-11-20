from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class Pagamento(TemplateView):
    def get(self, request):
        return render(request, 'pagamento/pagamento.html')