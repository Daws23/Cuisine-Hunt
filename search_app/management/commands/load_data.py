import csv
import json
from django.core.management.base import BaseCommand
from search_app.models import Restaurant, Dish

class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        with open('D:\Primenumbers Tech\\restaurant_search\\search_app\\assets\\restaurants_small.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    full_details = json.loads(row['full_details'])
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON for full_details: {row['full_details']}")
                    print(f"Skipping row due to error: {e}")
                    continue

                restaurant, created = Restaurant.objects.get_or_create(
                    name=row['name'],
                    location=row['location'],
                    lat_long=row['lat_long'],
                    full_details=full_details
                )

                try:
                    dishes = json.loads(row['items'])
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON for items: {row['items']}")
                    print(f"Skipping row due to error: {e}")
                    continue

                for dish_name, dish_price in dishes.items():
                    # Clean the dish_price to ensure it is a valid float
                    try:
                        price = float(dish_price.strip().split()[0])
                    except ValueError:
                        # Skip the dish if the price is not valid
                        continue

                    Dish.objects.create(
                        restaurant=restaurant,
                        name=dish_name,
                        price=price
                    )
