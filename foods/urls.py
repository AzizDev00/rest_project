from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, FoodViewSet,
    FoodReviewViewSet, FoodOrderViewSet,
    CourierViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'food-reviews', FoodReviewViewSet)
router.register(r'food-orders', FoodOrderViewSet)
router.register(r'couriers', CourierViewSet)

urlpatterns = router.urls
