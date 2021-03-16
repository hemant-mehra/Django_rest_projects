from django.shortcuts import render
from django.http import  request,response
from django.http import HttpResponse
# for serializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import  Movie,Rating
from .serializers import MovieSerializer,RatingSerializer,UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated,AllowAny

# Create your views here.

def http(request):
    return HttpResponse("hello world")

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class MoviesViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    @action(detail=True,methods=["POST"])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data:
            movie=Movie.objects.get(id=pk)
            stars=request.data['stars']
            user=request.user
            # user=User.objects.get(id=1)
            print(pk)
            print(movie.title)
            print(user.username)

            #update and create
            try:
                rating=Rating.objects.get(user=user.id,movie=movie.id)
                rating.stars=stars
                rating.save()
            except :
                rating=Rating.objects.create(user=user,movie=movie,stars=stars)
                

            response={'message':'its working'}
            return Response(response,status=status.HTTP_200_OK)
        else:
            response={'message':'please provide stars'}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

            
   

class RatingsViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response={'message':'default method of update is restricted by overwriting by me'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response={'message':'default method of create is restricted by overwriting by me'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)


