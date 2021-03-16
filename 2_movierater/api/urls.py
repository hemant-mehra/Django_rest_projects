from django.urls import path,include
from . import views
from .views import MoviesViewSet,RatingsViewSet,UserViewSet

# for rest framework
from rest_framework import routers

router=routers.DefaultRouter()
router.register('movies',MoviesViewSet)
router.register('ratings',RatingsViewSet)
router.register('users',UserViewSet)


urlpatterns = [
    path('new/',views.http),
    path("rest/",include(router.urls)),
]