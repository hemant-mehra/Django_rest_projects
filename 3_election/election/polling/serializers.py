from rest_framework import serializers
from polling.models import Candidate,Voter

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id','name','age')

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Voter
        fields=('id','name','adhaar_num','voted_for')

