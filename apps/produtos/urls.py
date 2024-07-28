from django.urls import path
from apps.produtos import fornecedoView, fabricante_view
from apps.produtos import fabricante_view
from apps.produtos import views

app_name = 'produtos'

urlpatterns = [
    path('fornecedores/', views.index, name='fornecedor'),
    path('fornecedores/list/', fornecedoView.list_fornecedor, name='fornecedor_list'),
    path('fornecedor/add', fornecedoView.add_fornecedor, name='add_fornecedor'),
    path('fornecedor/<uuid:pk>/remove', fornecedoView.remove_fornecedor, name='remove_fornecedor'),
    path('fornecedor/<uuid:pk>/edit', fornecedoView.edit_fornecedor, name='edit_fornecedor'),

    # fabricantes

    path('fabricantes/', fabricante_view.index, name='fabricantes'),
    path('fabricantes/list/', fabricante_view.list, name='fabricante_list'),
    path('faricante/add', fabricante_view.to_add, name='fabricante_add'),
    path('faricante/<uuid:pk>/edit', fabricante_view.edit, name='fabricante_edit'),
    path('faricante/<uuid:pk>/remove', fabricante_view.delete, name='fabricante_remove'),

    # produtos

    path('', views.index, name='produtos'),
    path('list/', views.list, name='produto_list'),
    path('add/', views.to_add, name='produto_add'),
    path('<uuid:pk>/edit/', views.edit, name='produto_edit'),
    path('<uuid:pk>/remove/', views.delete, name='produto_remove'),
]
