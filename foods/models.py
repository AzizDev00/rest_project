import uuid
from django.db import models
from shared.models import BaseModel

class Category(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Food(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, models.CASCADE, related_name='foods')
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    discounted_price_field = models.FloatField(null=True, blank=True)
    discount_percentage_field = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'food'
        verbose_name = 'food'
        verbose_name_plural = 'foods'

    def __str__(self):
        return self.name
    
    @property
    def discounted_price(self):
        if self.is_discounted and self.discount_percentage_field is not None:
            return self.price - (self.price * self.discount_percentage_field / 100)
        else:
            return self.price
    
    @property
    def discount_percentage(self):
        if self.is_discounted and self.discounted_price_field is not None:
            return (self.price - self.discounted_price_field) / self.price * 100
        else:
            return 0
        
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return None

class FoodReview(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(Food, models.CASCADE, related_name='reviews')
    user = models.ForeignKey('users.User', models.CASCADE, related_name='food_reviews')
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'food_review'
        verbose_name = 'food review'
        verbose_name_plural = 'food reviews'

    def __str__(self):
        return f'Review of {self.food.name} by {self.user.username}'
    
class FoodOrder(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(Food, models.CASCADE, related_name='orders')
    user = models.ForeignKey('users.User', models.CASCADE, related_name='food_orders')
    quantity = models.IntegerField(default=1)
    total_price_field = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'food_order'
        verbose_name = 'food order'
        verbose_name_plural = 'food orders'

    def __str__(self):
        return f'Order of {self.food.name} by {self.user.username}'
    
    @property
    def total_price(self):
        return self.food.price * self.quantity
