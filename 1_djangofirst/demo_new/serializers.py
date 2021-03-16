from rest_framework import serializers
from .models import Book,BookNumber,Character,Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=["id","name","surname"]


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields=["id","name"]

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNumber
        fields=["id","isbn_10","isbn_13"]

class BookSerializer(serializers.ModelSerializer):
    number=BookNumberSerializer(many=False)
    character=CharacterSerializer(many=True)
    author=AuthorSerializer(many=True)
    class Meta:
        model=Book
        fields=["id","title","description","price","is_published","number",'character','author']


class BookMiniSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Book
        fields=["id","title"]