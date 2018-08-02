from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.review, name='review')
]
