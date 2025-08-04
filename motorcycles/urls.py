from django.urls import path

from motorcycles import views

urlpatterns = [

    # PUBLIC VIEWS

    path('', views.MotorcycleListView.as_view(), name='motorcycle-list'),
    path('<int:pk>/', views.MotorcycleDetailView.as_view(), name='motorcycle-detail'),

    path('parts/', views.PartsListView.as_view(), name='parts-list'),
    path('parts/<int:pk>/', views.PartsDetailView.as_view(), name='parts-detail'),

    path('accessories/', views.AccessoriesListView.as_view(), name='accessories-list'),
    path('accessories/<int:pk>/', views.AccessoriesDetailView.as_view(), name='accessories-detail'),

    path('search/', views.UniversalSearchView.as_view(), name='search-results'),

    # PRIVATE VIEWS FOR CRUD

    path('create/', views.MotorcycleCreateView.as_view(), name='admin-motorcycle-create'),
    path('<int:pk>/edit/', views.MotorcycleUpdateView.as_view(), name='admin-motorcycle-edit'),
    path('<int:pk>/delete/', views.MotorcycleDeleteView.as_view(), name='admin-motorcycle-delete'),

    path('parts/create/', views.PartsCreateView.as_view(), name='parts-create'),
    path('parts/<int:pk>/edit/', views.PartsUpdateView.as_view(), name='parts-edit'),
    path('parts/<int:pk>/delete/', views.PartsDeleteView.as_view(), name='parts-delete'),

    path('accessories/create/', views.AccessoriesCreateView.as_view(), name='accessories-create'),
    path('accessories/<int:pk>/edit/', views.AccessoriesUpdateView.as_view(), name='accessories-edit'),
    path('accessories/<int:pk>/delete/', views.AccessoriesDeleteView.as_view(), name='accessories-delete'),
]
