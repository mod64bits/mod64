from django.urls import path

from . import views


app_name = 'produtos'

urlpatterns = [
    # categoria
    path('categoria/list', views.ProdutoCategoriaListView.as_view(), name='list-produto-categoria'),
    path('categoria/add/', views.ProdutoCategoriaCreateView.as_view(), name='create-produto-categoria'),
    path('categoria/update/<uuid:pk>/', views.ProdutoCategoriaUpdateView.as_view(), name='update-produto-categoria'),
    path('categoria/deletar/<uuid:pk>/', views.ProdutoCategoriaDeleteView.as_view(), name='delete-categoria-produto'),

    # fabricante

    path('fabricante/list', views.ProdutoFabricanteListView.as_view(), name='list-fabricante'),
    path('fabricante/add/', views.ProdutoFabricanteCreateView.as_view(), name='create-fabricante'),
    path('fabricante/update/<uuid:pk>/', views.ProdutoFabricanteUpdateView.as_view(), name='update-fabricante'),
    path('fabricante/deletar/<uuid:pk>/', views.ProdutoFabricanteDeleteView.as_view(), name='delete-fabricante'),

    # Produto

    path('', views.ProdutoListView.as_view(), name='list-produto'),
    path('add/', views.ProdutoCreateView.as_view(), name='create-produto'),
    path('update/<uuid:pk>/', views.ProdutoUpdateView.as_view(), name='update-produto'),
    path('deletar/<uuid:pk>/', views.ProdutoDeleteView.as_view(), name='delete-produto'),

]
