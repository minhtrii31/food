from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Restaurant, Menu, Order, Review

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'certified')
    list_filter = ('certified',)
    search_fields = ('name', 'address')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status')
    list_filter = ('status',)
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'totalPrice', 'status')
    list_filter = ('status',)
    search_fields = ('user__name', 'restaurant__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'rating')
    list_filter = ('rating',)
    search_fields = ('user__name', 'restaurant__name')
