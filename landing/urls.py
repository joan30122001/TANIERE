from django.urls import path, include
from .views import LandingViewSet
from landing import views




urlpatterns = [
    path("landing" , LandingViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
]