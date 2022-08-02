from django.urls import path
from bandas import views
from .views import home, crear_banda, about, listado_bandas, buscar, eliminar_bandas, mostrar_bandas, editar_bandas

urlpatterns = [
    path('crear-banda/', crear_banda, name='crear_banda'),
    path('listado-bandas/', listado_bandas, name='listado_bandas'),
    path('about/', about, name='about'),
    path('', home, name='home'),
    path('buscar/', buscar, name='buscador'),
    path('editar-bandas/<int:id>/', editar_bandas, name='editar_bandas'),
    path('eliminar-bandas/<int:id>/', eliminar_bandas, name='eliminar_bandas'),
    path('mostrar-bandas/<int:id>/', mostrar_bandas, name='mostrar_bandas'),
]
