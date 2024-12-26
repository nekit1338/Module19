"""
URL configuration for module19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('main', views.show_platform, name='main'),
    #  path('shop', views.show_shop, name='shop'),
    #  path('cart', views.show_cart, name='cart'),
    #  path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    #  path('cart/clear', views.clear_cart, name='clear_cart'),
    #  path('sign_up_html', views.sign_up_by_html, name='sign_up_html'),
    #  path('django_sign_up/', views.sign_up_by_django, name='sign_up_django'),
    path('', include('task1.urls')),
]
