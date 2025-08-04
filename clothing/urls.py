from django.urls import path

from clothing import views

urlpatterns = [
    path('', views.ClothingListView.as_view(), name='clothing-list'),
    path('<int:pk>/', views.ClothingDetailView.as_view(), name='clothing-detail'),
    path('create/', views.ClothingCreateView.as_view(), name='clothing-create'),
    path('<int:pk>/edit/', views.ClothingUpdateView.as_view(), name='clothing-edit'),
    path('<int:pk>/delete/', views.ClothingDeleteView.as_view(), name='clothing-delete'),
]
