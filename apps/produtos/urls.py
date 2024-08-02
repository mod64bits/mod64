from django.urls import path
from apps.produtos import fornecedoView
from apps.produtos import fabricante_view
from apps.produtos import views as produtos_views

app_name = 'produtos'

urlpatterns = [
    path('fornecedores/', fornecedoView.index, name='fornecedor'),
    path('fornecedores/list/', fornecedoView.list, name='fornecedor_list'),
    path('fornecedor/add/', fornecedoView.to_add, name='add_fornecedor'),
    path('edite/fornecedor/<uuid:pk>/', fornecedoView.edit, name='edit_fornecedor'),
    path('delete/fornecedor/<uuid:pk>/', fornecedoView.delete, name='remove_fornecedor'),

    # fabricantes

    path('fabricantes/', fabricante_view.index, name='fabricantes'),
    path('fabricantes/list/', fabricante_view.list, name='fabricante_list'),
    path('faricante/add/', fabricante_view.to_add, name='fabricante_add'),
    path('faricante/edit/<uuid:pk>/', fabricante_view.edit, name='fabricante_edit'),
    path('faricante/remove/<uuid:pk>/', fabricante_view.delete, name='fabricante_remove'),

    # produtos

    path('', produtos_views.index, name='produtos'),
    path('list/', produtos_views.list, name='produto_list'),
    path('add/', produtos_views.to_add, name='produto_add'),
    path('<uuid:pk>/edit/', produtos_views.edit, name='produto_edit'),
    path('<uuid:pk>/remove/', produtos_views.delete, name='produto_remove'),
]
