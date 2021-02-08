from django.views.generic import TemplateView


class ManutencaoView(TemplateView):
    template_name = 'setup/manutenção.html'


class IndexView(TemplateView):
    template_name = 'setup/index.html'
