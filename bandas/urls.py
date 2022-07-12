from django.urls import path
from .views import home, crear_banda, about, listado_bandas

urlpatterns = [
    path('crear-banda/', crear_banda, name='crear_banda'),
    path('listado-bandas/', listado_bandas, name='listado_bandas'),
    path('home', about, name='about'),
    path('', home, name='home'),
]
