from django.shortcuts import render, get_object_or_404, redirect

from movie.models import Movie
from .models import Review

# Create your views here.
def review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        Review.objects.create(
            movie=movie,
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        return redirect('search')
    result = {
        'movie': movie,
    }
    return render(request, 'review.html', result)
