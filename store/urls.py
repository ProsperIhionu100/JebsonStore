from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('product_page/<slug:slug>/', views.product_page, name='product_page'),
    
    path('category/<slug:slug>/', views.category, name='category'),
    
    path('shop/', views.shop, name='shop'),
    # path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('about_us/', views.about_us, name='about_us'),
    
]
