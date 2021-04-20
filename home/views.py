from django.shortcuts import render
from .models import GalleryImage
from reviews.models import Review
from django.core.paginator import Paginator

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


def gallery(request):
    gallery_images = GalleryImage.objects.all().order_by('-id')
    paginator = Paginator(gallery_images, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Gallery',
        'gallery_images': page_obj,
    }

    return render(request, 'home/gallery.html', context)


def contact(request):
    context = {
        'title': 'Contact',
    }

    return render(request, 'home/contact.html', context)
