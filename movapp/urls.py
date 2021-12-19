from django.urls import path
from movapp import views
from movieproject.views import GenreListView, MovieCreateView, MovieList, MovieDetailView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('movies/', MovieList.as_view()),
    path('add_movies/', MovieCreateView.as_view()),
    path('movie/<str:title>', MovieDetailView.as_view()),
    path('genre/', GenreListView.as_view())
]