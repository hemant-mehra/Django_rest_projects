from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer,BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

def Http(request):
    return HttpResponse('fucntion based Http response')

class First(View):
    books=Book.objects.all()
    def get(self,request):
        return render(request,"first.html",{"books":self.books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookMiniSerializer
    queryset=Book.objects.all()
    authentication_classes=(TokenAuthentication,)
    # permission_classes is used if we want the viewset
    # to be specificaly authenticated. thus we used allow
    # any in setting.py rest framework settings
    permission_classes=(IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


    