from django.contrib import admin
from .models import Category, Food, FoodReview, FoodOrder, Courier

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(FoodReview)
admin.site.register(FoodOrder)
admin.site.register(Courier)