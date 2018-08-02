from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.review, name='review'),
    path('<int:movie_id>/<int:review_id>/delete', views.review_delete, name='review_delete'),
    path('<int:movie_id>/<int:review_id>/edit', views.review_edit, name='review_edit')
]
