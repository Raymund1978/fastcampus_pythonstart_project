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


def review_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    get_review = get_object_or_404(movie.review_set, pk=review_id)
    get_review.delete()
    return redirect('review', movie_id=movie_id)


def review_edit(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    get_review = get_object_or_404(movie.review_set, pk=review_id)

    if request.method == 'POST':
        print(dir(get_review))
        get_review.title = request.POST.get('title')
        get_review.content = request.POST.get('content')
        get_review.save()
        return redirect('search')
    return render(request, 'edit.html', {
        'movie': movie,
        'review': get_review
    })
