from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Review
from .forms import ReviewCreationForm

# Create your views here.


def reviews(request):
    reviews = Review.objects.all().order_by('-id')
    review_form = ReviewCreationForm(
        initial={'name': 'A 101 Transfurmations Customer'})
    paginator = Paginator(reviews, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Reviews',
        'form': review_form,
        'reviews': page_obj,
    }

    if request.method == 'POST':
        review_form = ReviewCreationForm(request.POST)
        if review_form.is_valid():
            review_form.save()

        return redirect('reviews')

    return render(request, 'reviews/reviews.html', context)
