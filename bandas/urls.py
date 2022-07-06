from django.urls import path
from .views import home, un_template

urlpatterns = [
    path('', home),
    path('mi-template/', un_template),
]
