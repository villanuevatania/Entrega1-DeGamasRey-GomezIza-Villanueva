from django.urls import path
from .views import home, un_template, about

urlpatterns = [
    path('mi-template/', un_template, name='bandas'),
    path('home', about, name='about'),
    path('', home, name='home'),
]
