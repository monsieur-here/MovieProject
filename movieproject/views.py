from django.shortcuts import render
# Create your views here.

from movapp.models import Movie, Genre, userLogin
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from movapp.serializers import GenreSerializer, MovieSerializer, userLoginSerializer
from rest_framework.pagination import PageNumberPagination

class MovieList(ListAPIView):

    permission_classes = (AllowAny, )

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        qs = userLogin.objects.all()
        serializer_class = userLoginSerializer(qs, many=True)
        return Response(serializer_class.data)
    
    def post(self, request, *args, **kwargs):
        serializer_class = userLoginSerializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors)

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
    pagination_class = PageNumberPagination