from django.contrib import admin
from django.urls import path, include

from .views import IndexView, AulaDeAutomacaoView, CarrinhoView, ContatoView, MoveUpConstrutechView, PlanosEPrecosView, \
    SimuladorView

app_name = 'construtech'

urlpatterns = [
    # path('', include('sidtm.urls')),
    # path('', ManutencaoView.as_view(), name='manutencao'),
    path('', IndexView.as_view(), name='index'),
    path('aula-de-automacao/', AulaDeAutomacaoView.as_view(), name='aula-de-automacao'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('move-up-construtech/', MoveUpConstrutechView.as_view(), name='move-up-construtech'),
    path('planos-e-precos/', PlanosEPrecosView.as_view(), name='planos-e-precos'),
    path('simulador', SimuladorView.as_view(), name='simulador'),

]
