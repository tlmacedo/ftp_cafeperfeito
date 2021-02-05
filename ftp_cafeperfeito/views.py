from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'cafeperfeito/about.html'


class BlogView(TemplateView):
    template_name = 'cafeperfeito/blog.html'


class BlogSingleView(TemplateView):
    template_name = 'cafeperfeito/blog-single.html'


class CartView(TemplateView):
    template_name = 'cafeperfeito/cart.html'


class CheckOutView(TemplateView):
    template_name = 'cafeperfeito/checkout.html'


class ContactView(TemplateView):
    template_name = 'cafeperfeito/contact.html'


class GalleryView(TemplateView):
    template_name = 'cafeperfeito/gallery.html'


class IndexView(TemplateView):
    template_name = 'cafeperfeito/index.html'


class MenuView(TemplateView):
    template_name = 'cafeperfeito/menu.html'


class ProductSingleView(TemplateView):
    template_name = 'cafeperfeito/product-single.html'


class RoomView(TemplateView):
    template_name = 'cafeperfeito/room.html'


class ServicesView(TemplateView):
    template_name = 'cafeperfeito/services.html'


class ShopView(TemplateView):
    template_name = 'cafeperfeito/shop.html'
