from rest_framework.routers import DefaultRouter

from api_v1.views.autos import AutoViewSet

router = DefaultRouter()
router.register(r'auto', AutoViewSet, 'autos')

urlpatterns = router.urls