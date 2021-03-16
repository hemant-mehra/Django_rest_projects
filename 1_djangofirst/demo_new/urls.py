from django.urls import path,include
from . import views
from .views import First

# for rest framework
from rest_framework import routers
from .views import BookViewSet

# for restframework
router=routers.DefaultRouter()
router.register("book",BookViewSet)

urlpatterns = [
    path('http/',views.Http),
    path("first/",First.as_view()),
    path("rest/",include(router.urls))
    
]