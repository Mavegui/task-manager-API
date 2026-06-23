import rest_framework_simplejwt.views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.tasks.views import RegisterView

urlpatterns = [
    #URL derivada de apps/tasks.
    path("api/v1/", include("apps.tasks.urls")),
    
    #Login via web e user register
    path("api-auth/", include("rest_framework.urls")), #Deixando passar, mas removeria em prod.
    path("api/v1/register/", RegisterView.as_view(), name="auth_register"),    
    
    #Token
    path("api/v1/token/", rest_framework_simplejwt.views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", rest_framework_simplejwt.views.TokenRefreshView.as_view(), name="token_refresh"),

    #Painel admin Django
    path("admin/", admin.site.urls),
]


if settings.ENABLE_API_DOCS:
    urlpatterns += [
        #Swagger UI
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    ]