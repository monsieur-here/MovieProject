from django.urls import path
from movieproject.views import GenreListView, MovieCreateView, MovieList, MovieDetailView
from . import views


urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('add_movies/', MovieCreateView.as_view()),
    path('movie/<str:title>', MovieDetailView.as_view()),
    path('genre/', GenreListView.as_view()),
    # path('collection/', )
    # path('collection/<collection_uuid>', )
]