from django.contrib import admin
from .models import Restaurant, Dish

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'lat_long', 'average_rating')
    search_fields = ('name', 'location')

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'restaurant')
    search_fields = ('name', 'restaurant__name')
    list_filter = ('restaurant',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Dish, DishAdmin)
