from django.urls import path
from cart import views

urlpatterns = [
    path('add/<int:content_type_id>/<int:object_id>/', views.add_to_cart, name='add-to-cart'),
    path('', views.cart_detail, name='cart-detail'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update-cart-item'),
    path('clear/', views.clear_cart, name='clear-cart'),
    path('checkout/', views.checkout, name='checkout'),  # Add this
    path('success/', views.checkout_success, name='checkout-success'),  # Add this
]
