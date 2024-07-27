from django.urls import path
from apps.produtos import fornecedoView
from apps.produtos import fabricante_view

app_name = 'produtos'

urlpatterns = [
    path('fornecedores/', fornecedoView.index_fornecedor, name='fornecedor'),
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
]
