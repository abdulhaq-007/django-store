from django.urls import  path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("<int:p_id>/detail/", views.detail, name='detail'),
    path('shop/', views.ShopView, name='shop'),

]