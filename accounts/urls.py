from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterView, ProfileDetailView, ProfileUpdateView,
    MotorcycleCreateView, MotorcycleUpdateView, MotorcycleDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('motorcycle/add/', MotorcycleCreateView.as_view(), name='motorcycle-add'),
    path('motorcycle/<int:pk>/edit/', MotorcycleUpdateView.as_view(), name='motorcycle-edit'),
    path('motorcycle/<int:pk>/delete/', MotorcycleDeleteView.as_view(), name='motorcycle-delete'),
]
