from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile-edit'),
    path('motorcycle/add/', views.MotorcycleCreateView.as_view(), name='motorcycle-add'),
    path('motorcycle/<int:pk>/edit/', views.MotorcycleUpdateView.as_view(), name='motorcycle-edit'),
    path('motorcycle/<int:pk>/delete/', views.MotorcycleDeleteView.as_view(), name='motorcycle-delete'),
    path('find-my-bike/', views.FindMyBikeView.as_view(), name='find-my-bike'),
    path('find-my-clothing/', views.FindMyClothingView.as_view(), name='find-my-clothing'),
]
