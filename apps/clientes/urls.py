from django.urls import path

from . import views


app_name = 'clientes'

urlpatterns = [
    path('', views.ClienteListView.as_view(),  # list view not handled here
        name='list-cliente'
    ),
    path('add/', views.ClienteCreateView.as_view(),  # list view not handled here
        name='create-cliente'
    ),
    path('update/<uuid:pk>', views.ClienteUpdateView.as_view(),
        name='update_cliente'
     ),
    path('deletar/<uuid:pk>/', views.ClienteDeleteView.as_view(),
         name='cliente_delete'
         ),


]
