from django.urls import path

from . import views


app_name = 'tickets'

urlpatterns = [
    # categoria
    path('categoria/list', views.TicketListView.as_view(), name='list-tickets'),
    path('ticket/add/', views.TicketCreateView.as_view(), name='abrir-ticket'),
    #path('categoria/update/<uuid:pk>/', views.ProdutoCategoriaUpdateView.as_view(), name='update-produto-categoria'),
    #path('categoria/deletar/<uuid:pk>/', views.ProdutoCategoriaDeleteView.as_view(), name='delete-categoria-produto'),

]
