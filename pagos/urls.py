# pagos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_pago, name='crear_pago'),
    path('pago/listar/', views.listar_pagos, name='listar_pagos'),
    path('editar/<int:pk>/', views.editar_pago, name='editar_pago'),
    path('eliminar/', views.eliminar_pago, name='eliminar_pago'),
]
