from django.urls import path
from .import views


urlpatterns = [
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
    path("validacupom/", views.validacupom, name='validacupom'),

]
