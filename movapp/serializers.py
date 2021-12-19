from django.db.models import fields
from rest_framework import serializers
from .models import Genre, Movie, userLogin

class userLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=userLogin
        fields=[
            'name', 'password'
        ]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['name',]
