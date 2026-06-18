import rest_framework_simplejwt.views
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.tasks.views import RegisterView

urlpatterns = [
    #URL derivada de apps/tasks.
    path("api/v1/", include("apps.tasks.urls")),
    
    #Endpoint que o DRF usa para login via web e Endpoint que registra user
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/register/", RegisterView.as_view(), name="auth_register"),    
    
    #Token Endpoints
    path("api/v1/token/", rest_framework_simplejwt.views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", rest_framework_simplejwt.views.TokenRefreshView.as_view(), name="token_refresh"),
    
    #Swagger EndPoints
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    
    #Painel admin Django
    path("admin/", admin.site.urls),
]