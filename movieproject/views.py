from django.shortcuts import render
# Create your views here.

from movapp.models import Movie, Genre
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from movapp.serializers import GenreSerializer, MovieSerializer

class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateView(CreateAPIView):

    permission_classes = (AllowAny, )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    lookup_field = 'title'
    serializer_class = MovieSerializer

class GenreListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer