from django.urls import path,include
from rest_framework import routers
from polling import views
from polling.views import CandidateViewSet,VoterViewSet
from polling.views import CandidateList

router=routers.DefaultRouter()
router.register('can',CandidateViewSet)
router.register('voter',VoterViewSet)

urlpatterns = [  
    path('test/',views.http) ,
    path('',include(router.urls)),
    path('main/',CandidateList.as_view(),name='main')
    
]
