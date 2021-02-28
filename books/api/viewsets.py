from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer #pegando a classe do arquivo serializers.py que foi criada antes.
    queryset = models.Books.objects.all() # todos os objetos que estão dentro do meu model.Books





