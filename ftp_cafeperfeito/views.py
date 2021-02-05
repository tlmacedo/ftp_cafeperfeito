from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'cafeperfeito/index.html'


class MenuView(TemplateView):
    template_name = 'cafeperfeito/menu.html'


class ServicesView(TemplateView):
    template_name = 'cafeperfeito/services.html'


class BlogView(TemplateView):
    template_name = 'cafeperfeito/blog.html'


class AboutView(TemplateView):
    template_name = 'cafeperfeito/about.html'


class ContactView(TemplateView):
    template_name = 'cafeperfeito/contact.html'
