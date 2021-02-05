from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class BlogSingleView(TemplateView):
    template_name = 'blog-single.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class CheckOutView(TemplateView):
    template_name = 'checkout.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class GalleryView(TemplateView):
    template_name = 'gallery.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class ProductSingleView(TemplateView):
    template_name = 'product-single.html'


class RoomView(TemplateView):
    template_name = 'room.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class ShopView(TemplateView):
    template_name = 'shop.html'
