from django.urls import path
from .import views

app_name = 'cart'
    
urlpatterns = [
    path('', views.cartView, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path('add/', views.addToCart , name='add'),
    path('add/qty/', views.addToCartQty , name='addQty'),
    path('remove/', views.removeCartItems , name='removeAllItems'),
    path('delete/<int:product_id>/qty/<int:qty>', views.deleteCartItem , name='delete'),
]