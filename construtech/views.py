from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'construtech/index.html'


class AulaDeAutomacaoView(TemplateView):
    template_name = 'construtech/aula-de-automacao.html'


class CarrinhoView(TemplateView):
    template_name = 'construtech/carrinho.html'


class ContatoView(TemplateView):
    template_name = 'construtech/contato.html'


class MoveUpConstrutechView(TemplateView):
    template_name = 'construtech/move-up-construtech.html'


class PlanosEPrecosView(TemplateView):
    template_name = 'construtech/planos-e-precos.html'


class SimuladorView(TemplateView):
    template_name = 'construtech/simulador.html'
