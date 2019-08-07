from django.urls import path
from django.conf.urls import include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedItemViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)),
]