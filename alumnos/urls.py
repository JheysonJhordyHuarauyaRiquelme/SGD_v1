# alumnos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alumnos, name='listar_alumnos'),  # Para listar alumnos
    path('nuevo/', views.crear_alumno, name='crear_alumno'),  # Para crear un nuevo alumno
    path('editar/<int:pk>/', views.editar_alumno, name='editar_alumno'),  # Para editar un alumno
    path('eliminar/<int:pk>/', views.eliminar_alumno, name='eliminar_alumno'),  # Para eliminar un alumno
]

