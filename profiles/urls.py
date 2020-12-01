from django.urls import path

from profiles import views

urlpatterns = [
    path('random-view', views.RandomApiView.as_view()),
]