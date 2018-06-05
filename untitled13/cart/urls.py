from django.conf.urls import *
from django.urls import path
from django import views

# urlpatterns = ('untitled13.cart.views',
# ('show_cart', {'template_name': 'cart/cart.html'}), 'show_cart'),

urlpatterns = [
    path('show_cart',
         views.cart, name='show_cart')
]
