from rest_framework import serializers
from .models import Category, Food, FoodReview, FoodOrder
from users.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    image_url = serializers.SerializerMethodField()
    discounted_price = serializers.FloatField(read_only=True)
    discount_percentage = serializers.FloatField(read_only=True)

    class Meta:
        model = Food
        fields = ['id', 'name', 'category', 'category_id', 'price', 'description', 'image', 'is_available', 
                  'is_popular', 'is_new', 'is_discounted', 'discount_percentage_field', 'created_at', 'updated_at', 
                  'image_url', 'discounted_price', 'discount_percentage']

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
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = FoodOrder
        fields = ['id', 'food', 'food_id', 'quantity', 'total_price', 'user', 'created_at']

    def get_total_price(self, obj):
        return obj.total_price

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
