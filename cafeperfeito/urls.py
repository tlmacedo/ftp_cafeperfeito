from django.urls import path

from ftp_cafeperfeito.views import IndexView

app_name = 'cafeperfeito'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
