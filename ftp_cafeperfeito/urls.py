"""ftp_cafeperfeito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ftp_cafeperfeito.views import IndexView, MenuView, ServicesView, BlogView, AboutView, ContactView, ShopView, \
    ProductSingleView, RoomView, CheckOutView, BlogSingleView, CartView, GalleryView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-single/', BlogSingleView.as_view(), name='blog-single'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('', IndexView.as_view(), name='index'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('product-single/', ProductSingleView.as_view(), name='product-single'),
    path('room/', RoomView.as_view(), name='room'),
    path('services/', ServicesView.as_view(), name='services'),
    path('shop/', ShopView.as_view(), name='shop'),

    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.STATIC_URL, documento_root=settings.STATIC_ROOT)
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
