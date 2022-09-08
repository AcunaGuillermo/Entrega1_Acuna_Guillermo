from django.urls import path
from AppFutbol import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    # URLs de Equipos
    path('equipos/', views.equipos, name="equipo"),
    path('crear-equipo/', views.crear_equipo, name="crear_equipo"),
    path('busqueda-equipo-form/', views.busqueda_equipos, name="busqueda_equipo_form"),
    path('busqueda-equipo/', views.buscar_equipo, name="busqueda_equipo"),
    # URLs de Jugadores
    path('Jugadores/', views.jugadores, name="jugador"),
    path('crear-jugador/', views.crear_jugador, name="crear_jugador"),
    path('editar-jugador/<int:id>/', views.editar_jugador, name="editar_jugador"),
    path('eliminar-jugador/<int:id>/', views.eliminar_jugador, name="eliminar_jugador"),
    # URLs de Posiciones
    path('Posiciones/', views.posiciones, name="posicion"),
    path('crear-posicion/', views.crear_posicion, name="crear_posicion"),
    path('editar-posicion/<int:id>/', views.editar_posicion, name="editar_posicion"),
    path('eliminar-posicion/<int:id>/', views.eliminar_posicion, name="eliminar_posicion"),
]
