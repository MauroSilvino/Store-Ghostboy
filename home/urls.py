from django.urls import path
from home.views import Home, LoginModal, Contato
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('entrar/', LoginModal.as_view(), name='loginmodal'),
    path('contato/', Contato.as_view(), name='contato'),
]