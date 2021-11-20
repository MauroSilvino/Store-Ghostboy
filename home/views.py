from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    def get(self, request):
        return render(request, 'home/home.html')

class LoginModal(TemplateView):
    def get(self, request):
        return render(request, 'home/login_register_modal.html')

class Contato(TemplateView):
    def get(self, request):
        return render(request, 'home/contact.html')
