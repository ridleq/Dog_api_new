from rest_framework import routers

from .views import BreedViewSet, DogViewSet

router = routers.DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breed')
router.register(r'dogs', DogViewSet, basename='dog')

urlpatterns = router.urls
