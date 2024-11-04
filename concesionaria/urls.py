from django.contrib import admin
from django.urls import path, include
from home.views import index_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API de Concesionaria",
      default_version='v1',
      description="Documentación de la API para la gestión de autos, clientes y comentarios",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="m.ison@itecriocuarto.org.ar"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path("", index_view, name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('autos/', include('gestion_autos.urls')),
    path('api_v1/', include('api_v1.urls')),
    
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
