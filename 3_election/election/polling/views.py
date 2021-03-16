from django.shortcuts import render
from django.shortcuts import get_object_or_404
from polling.serializers import CandidateSerializer,VoterSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from polling.models import Candidate,Voter
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.

def http(request):
    return HttpResponse('hello world')

class CandidateViewSet(viewsets.ModelViewSet):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer

    

class VoterViewSet(viewsets.ModelViewSet):
    queryset=Voter.objects.all()
    serializer_class=VoterSerializer


class CandidateList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main.html'

    def get(self, request):
        candidates = Candidate.objects.all()
        return Response({'candidates': candidates})