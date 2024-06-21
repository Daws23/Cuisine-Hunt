from django.core.management.base import BaseCommand
from search_app.models import Restaurant

class Command(BaseCommand):
    ''''Populate the average_rating field from full_details'''

    def handle(self, *args, **kwargs):
        restaurants = Restaurant.objects.all()
        for restaurant in restaurants:
            if 'user_rating' in restaurant.full_details:
                rating = restaurant.full_details['user_rating'].get('aggregate_rating')
                if rating:
                    restaurant.average_rating = float(rating)
                    restaurant.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated average_rating'))
