from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
