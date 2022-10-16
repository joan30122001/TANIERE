"""taniere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from allauth.account.views import confirm_email
from rest_framework import permissions # 2
from dj_rest_auth.registration.views import VerifyEmailView,ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "LA TANIERE",
        default_version = "v1",
        description = "Application pour les informations football au Cameroun",
        terms_of_service = "",
        contact = openapi.Contact(email = "xxxxxxxxxx@gmail.com"),
        License = openapi.License(name = "Beta License"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/football/', include('football.urls')),
    path('api/landing/', include('landing.urls')),
    path('api/auth/', include('auth.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('account/', include('allauth.urls')),
    # path('accounts-rest/registration/account-confirm-email/(?P<key>.+)/', confirm_email, name='account_confirm_email'),
    path('documentation', schema_view.with_ui('swagger', cache_timeout=0), name = "schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout = 0), name = "schema-swagger-ui"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "LA TANIERE ADMINISTRATION"
admin.site.site_title = "LA TANIERE ADMINISTRATION"
admin.site.index_title = "LA TANIERE ADMINISTRATION"