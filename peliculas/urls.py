from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('director/listado/', views.DirectorLista.as_view(), name="lista"),
    path('director/<int:pk>/', views.DirectorBuscar.as_view(), name="buscar"),
    path('director/registrar/', views.DirectorRegistrar.as_view(), name="registrar"),
    path('director/editar/<int:id>', views.DirectorEditar.as_view(), name="editar"),
    path('director/eliminar/<int:id>/', views.DirectorEliminar.as_view),
    path('pelicula/listado/', views.PeliculaConDirector.as_view()),
    path('pelicula/registrar/', views.PeliculaRegistrar.as_view()),
    path('pelicula/<int:id>/', views.PeliculaBuscar.as_view(), name="buscarPelicula"),
    path('pelicula/editar/<int:id>', views.PeliculaEditar.as_view(), name="editarPelicula"),
    path('pelicula/eliminar/<int:id>', views.PeliculaEliminar.as_view(), name="eliminarPelicula"),
]
