from django.shortcuts import render
from .models import GalleryImage
from reviews.models import Review

# Create your views here.


def home(request):
    gallery_images = GalleryImage.objects.all().order_by('-id')
    reviews = Review.objects.all().order_by('-id')
    context = {
        'title': 'Home',
        'gallery_images': gallery_images[:6],
        'reviews': reviews[:6],
    }

    return render(request, 'home/index.html', context)
