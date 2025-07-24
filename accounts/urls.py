from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterView, ProfileDetailView, ProfileUpdateView,
    MotorcycleCreateView, MotorcycleUpdateView, MotorcycleDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('motorcycle/add/', MotorcycleCreateView.as_view(), name='motorcycle_add'),
    path('motorcycle/<int:pk>/edit/', MotorcycleUpdateView.as_view(), name='motorcycle_edit'),
    path('motorcycle/<int:pk>/delete/', MotorcycleDeleteView.as_view(), name='motorcycle_delete'),
]
