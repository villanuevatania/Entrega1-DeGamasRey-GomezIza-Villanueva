from django.urls import path
from .views import posteo

urlpatterns = [
    path('post/', posteo, name='posteo')
]
