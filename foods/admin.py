from django.contrib import admin
from .models import Category, Food, FoodReview, FoodOrder, Courier

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(FoodReview)
admin.site.register(FoodOrder)


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'vehicle_type', 'user')