from django.shortcuts import render
from myapp import models
from rest_framework import serializers
from rest_framework import viewsets

class BooksSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'


class BooksViewSet (viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = models.Books.objects.all()



    