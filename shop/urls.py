from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    # path("<int:pk>/detail/", views.ProductDetailView.as_view(), name='detail')
    path("detail/<int:p_id>/", views.detail, name='detail'),
    path("detail/tag/<int:category_id>", views.tag_shop, name='tag'),
    path("shop/products/", views.ShopView.as_view(), name='shop'),
    # path("contact/", views.contact_view, name='contact')

]