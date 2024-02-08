from django.urls import path
from .import views


urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('produto/<int:id>', views.produto, name='produto'),
    path("categoria/<int:id>", views.categorias, name='categoria'),
    path('add_carrinho/', views.add_carrinho, name='add_carrinho'),
    path("ver_carrinho/", views.ver_carrinho, name='ver_carrinho'),
    path('remover_produto/<int:id>', views.remover_produto, name='remover_produto'),
]
