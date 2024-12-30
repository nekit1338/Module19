from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.show_platform, name='main'),
    path('shop', views.show_shop, name='shop'),
    path('cart', views.show_cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart/clear', views.clear_cart, name='clear_cart'),
    path('sign_up_html', views.sign_up_by_html, name='sign_up_html'),
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_django'),
    path('platform/news', views.show_news, name='news'),
]
