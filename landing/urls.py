from django.urls import path, include
from .views import LandingViewSet
from landing import views




router = routers.DefaultRouter()
router.register('user', views.UserView)

urlpatterns = [
    path("landing" , LandingViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
]