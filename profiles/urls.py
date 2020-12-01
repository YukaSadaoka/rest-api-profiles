from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles import views

router = DefaultRouter()
router.register('message-viewset', views.MessageViewSet, base_name='message-viewset')
urlpatterns = [
    path('random-view', views.RandomApiView.as_view()),
    path('', include(router.urls))
]