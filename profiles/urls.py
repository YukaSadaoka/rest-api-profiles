from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles import views

router = DefaultRouter()
router.register('message-viewset', views.MessageViewSet, base_name='message-viewset')
router.register('profile', views.UserProfileViewSet) ## don't need to give base_name because UserProfileViewSet has queryset

urlpatterns = [
    path('random-view', views.RandomApiView.as_view()),
    path('', include(router.urls))
]