from django.urls import path
from . import views

# Create your URLs here.

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
]
