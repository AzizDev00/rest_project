from rest_framework import viewsets, permissions
from .models import Category, Food, FoodReview, FoodOrder
from .serializers import CategorySerializer, FoodSerializer, FoodReviewSerializer, FoodOrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]

class FoodReviewViewSet(viewsets.ModelViewSet):
    queryset = FoodReview.objects.all()
    serializer_class = FoodReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FoodOrderViewSet(viewsets.ModelViewSet):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)