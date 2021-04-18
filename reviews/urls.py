from django.urls import path
from . import views

# Create your URLs here.


urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
]
