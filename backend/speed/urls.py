from django.urls import path
from .views import LatestSpeedView

urlpatterns = [
    path("latest/", LatestSpeedView.as_view()),
]
