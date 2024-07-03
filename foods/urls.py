from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, FoodViewSet,
    FoodReviewViewSet, FoodOrderViewSet,
    CourierViewSet, CustomTokenObtainPairView, RegisterCourierView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'food-reviews', FoodReviewViewSet)
router.register(r'food-orders', FoodOrderViewSet)
router.register(r'couriers', CourierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterCourierView.as_view(), name='register_courier'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

