from django.urls import path
from . import views

urlpatterns = [
    #----------------estudiantes-----------------
    path('', views.homeEstudiantes),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('edicionEstudiante/<cedula>', views.edicionEstudiante),
    path('editarEstudiante/', views.editarEstudiante),
    path('eliminarEstudiante/<cedula>', views.eliminarEstudiante),

    #----------------academicos-----------------
    path('ac/', views.homeAcademicos),
    path('registrarAcademico/', views.registrarAcademico),
    path('edicionAcademico/<cedula>', views.edicionAcademico),
    path('editarAcademico/', views.editarAcademico),
    path('eliminarAcademico/<cedula>', views.eliminarAcademico),

    #----------------administrativos-----------------
    path('ad/', views.homeAdministrativos),
    path('registrarAdministrativo/', views.registrarAdministrativo),
    path('edicionAdministrativo/<cedula>', views.edicionAdministrativo),
    path('editarAdministrativo/', views.editarAdministrativo),
    path('eliminarAdministrativo/<cedula>', views.eliminarAdministrativo),

    #---------------------libros---------------------
    path('li/', views.homeLibros),
    path('registrarLibro/', views.registrarLibro),
    path('edicionLibro/<codigolibro>', views.edicionLibro),
    path('editarLibro/', views.editarLibro),
    path('eliminarLibro/<codigolibro>', views.eliminarLibro),

    #---------------------prestamos---------------------
    path('pre/', views.homePrestamos),
    path('registrarPrestamo/', views.registrarPrestamo),
    path('edicionPrestamo/<codigo>', views.edicionPrestamo),
    path('editarPrestamo/', views.editarPrestamo),
    path('eliminarPrestamo/<codigo>', views.eliminarPrestamo),

    #-------------------salir--------------------
    path("cerrar/", views.cerrar, name="cerrar"),
]