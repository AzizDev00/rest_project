from rest_framework import serializers
from .models import Category, Food, FoodReview, FoodOrder, Courier
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image_url


class FoodReviewSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='food', write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = FoodReview
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class FoodOrderSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='food', write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    courier = serializers.StringRelatedField(read_only=True)
    courier_id = serializers.PrimaryKeyRelatedField(queryset=Courier.objects.all(), source='courier', write_only=True, required=False)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = FoodOrder
        fields = ['id', 'food', 'food_id', 'quantity', 'total_price', 'user', 'user_id', 'courier', 'courier_id', 'status', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        food = validated_data['food']
        quantity = validated_data.get('quantity', 1)
        validated_data['user'] = user
        validated_data['total_price_field'] = food.price * quantity
        return super().create(validated_data)


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class RegisterCourierSerializer(serializers.ModelSerializer):
    courier_name = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    vehicle_type = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'courier_name', 'phone_number', 'vehicle_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        courier_name = validated_data.pop('courier_name')
        phone_number = validated_data.pop('phone_number')
        vehicle_type = validated_data.pop('vehicle_type')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        
        Courier.objects.create(
            user=user,
            name=courier_name,
            phone_number=phone_number,
            vehicle_type=vehicle_type
        )
        
        return user