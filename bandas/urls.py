from django.urls import path
from bandas import views
from .views import home, crear_banda, about, listado_bandas, buscar, editar_banda, eliminar_banda

urlpatterns = [
    path('', home, name='home'),
    path('crear-banda/', crear_banda, name='crear_banda'),
    path('listado-bandas/', listado_bandas, name='listado_bandas'),
    path('about/', about, name='about'),
    path('buscar/', buscar, name='buscador'),
    path('editar-banda/<int:id>/', editar_banda, name='editar_banda'),
    path('eliminar-banda/<int:id>/', eliminar_banda, name='eliminar_banda'),
]