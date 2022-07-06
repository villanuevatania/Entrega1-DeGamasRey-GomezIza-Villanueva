from django.urls import path
from .views import home, crear_banda, about

urlpatterns = [
    path('mi-template/', crear_banda, name='crear_banda'),
    path('home', about, name='about'),
    path('', home, name='home'),
]
