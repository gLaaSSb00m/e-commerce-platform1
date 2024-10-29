"""
URL configuration for ecommerce project.

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
from django.urls import path
from core import views
urlpatterns = [
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('blog',views.blog,name='blog'),
    path('faq',views.faq,name='faq'),
    path('privacy-policy',views.privacy_policy,name='privacy_policy'),
    path('my-account',views.my_account,name='my_account'),
    path('login',views.login,name='login'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('empty-cart',views.empty_cart,name='empty_cart'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('compare',views.compare,name='compare'),
    path('about-us',views.about_us,name='about_us'),
    path('contact-us',views.contact_us,name='contact_us'),
    path('admin/', admin.site.urls),
    
]
