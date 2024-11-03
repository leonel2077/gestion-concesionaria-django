from django.contrib import admin
from django.urls import path, include
from home.views import index_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
