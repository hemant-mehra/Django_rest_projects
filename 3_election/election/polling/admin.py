from django.contrib import admin
from polling.models import Candidate,Voter

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Voter)
