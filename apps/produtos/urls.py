from django.urls import path
from apps.produtos import fornecedoView

app_name = 'produtos'

urlpatterns = [
    path('fornecedores/', fornecedoView.index_fornecedor, name='fornecedor'),
    path('fornecedores/list/', fornecedoView.list_fornecedor, name='fornecedor_list'),
    path('fornecedor/add', fornecedoView.add_fornecedor, name='add_fornecedor'),
    path('fornecedor/<uuid:pk>/remove', fornecedoView.remove_fornecedor, name='remove_fornecedor'),
    path('fornecedor/<uuid:pk>/edit', fornecedoView.edit_fornecedor, name='edit_fornecedor'),
]
