from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Food, FoodReview, FoodOrder, Courier
from .serializers import (
    CategorySerializer, FoodSerializer,
    FoodReviewSerializer, FoodOrderSerializer,
    CourierSerializer  
)

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

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def pick_up(self, request, pk=None):
        order = self.get_object()
        if order.status != FoodOrder.PENDING:
            return Response({'status': 'Order is not available for pickup.'}, status=status.HTTP_400_BAD_REQUEST)
        
        order.courier = request.user.courier  # Assuming the user is a courier and has a related Courier object
        order.status = FoodOrder.IN_PROGRESS
        order.save()
        return Response({'status': 'Order picked up and in progress.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def deliver(self, request, pk=None):
        order = self.get_object()
        if order.status != FoodOrder.IN_PROGRESS:
            return Response({'status': 'Order is not in progress.'}, status=status.HTTP_400_BAD_REQUEST)
        
        order.status = FoodOrder.DELIVERED
        order.save()
        return Response({'status': 'Order delivered.'}, status=status.HTTP_200_OK)

class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [permissions.AllowAny]
