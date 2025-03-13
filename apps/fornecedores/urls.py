from django.urls import path

from . import views


app_name = 'fornecedores'

urlpatterns = [
    path('', views.FornecedorListView.as_view(), name='list-fornecedor'),
    path('add/', views.FornecedorCreateView.as_view(), name='create-fornecedor'),
    path('update/<uuid:pk>', views.FornecedorUpdateView.as_view(), name='update_fornecedor'
     ),
    path('deletar/<uuid:pk>/', views.FornecedorDeleteView.as_view(),
         name='delete-fornecedor'
         ),


]
