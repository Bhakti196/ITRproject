from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EstimateViewSet, BOQItemViewSet
router = DefaultRouter()
router.register("estimates", EstimateViewSet, basename="estimate")
router.register("boq-items", BOQItemViewSet, basename="boq-item")
urlpatterns = [path("", include(router.urls))]
