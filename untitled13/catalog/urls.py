from django.urls import path
from django import views

urlpatterns = [

    path('index/',
         views.index,name='index'),
    path('show_category/<category_slug>/',
         views.show_category,name='category'),
    path('show_product/<product_slug>/',
         views.show_product,name='show_product')
]
