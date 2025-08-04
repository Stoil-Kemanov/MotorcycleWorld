from django.urls import path

from services import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('create/', views.ServiceCreateView.as_view(), name='service-create'),
    path('<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service-edit'),
    path('<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service-delete'),
]
