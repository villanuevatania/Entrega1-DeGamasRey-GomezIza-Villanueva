from django.urls import path
from .views import home, crear_banda, about, listado_bandas

urlpatterns = [
    path('mi-template/', crear_banda, name='crear_banda'),
    path('mi-template/', listado_bandas, name='listado_bandas'),
    path('home', about, name='about'),
    path('', home, name='home'),
]
