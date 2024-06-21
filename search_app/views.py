from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from search_app.models import Dish, Restaurant
import re

def search(request):
    query = request.GET.get('q', '')  
    original_query = query
    veg_only = request.GET.get('veg_only', '') 

    # To exclude non_veg food items for veg guys
    non_veg_keywords = ["chicken", "beef", "mutton", "fish", "crab", "prawn", "pork", "quail", "lamb", "lobster", "shrimp", "shawarma", "hummus"]

    results = Dish.objects.select_related('restaurant').all()

    if query:
        # A multiword query analysis where numbers are assumed to represent cost
        # the words following it represent restaurant name and dish or the other way around

        price_match = re.search(r'\b\d+\b', query)
        if price_match:
            price = int(price_match.group())
            query = query.replace(str(price), '').strip()
        else:
            price = None

        words = query.split()

        possible_dish = ""
        possible_restaurant = ""

        # This is to check if restaurant name follows the dish name
        for i in range(len(words)):
            test_dish = " ".join(words[:i+1])
            test_restaurant = " ".join(words[i:])

            if Dish.objects.filter(name__icontains=test_dish).exists():
                possible_dish = test_dish
            else:
                possible_restaurant = test_restaurant
                break
        
        possible_dish1 = ""
        possible_restaurant1 = ""

        # This is to check if dish name follows the restaurant name
        for i in range(len(words)):
            test_restaurant = " ".join(words[:i+1])
            test_dish = " ".join(words[i:])

            if Restaurant.objects.filter(name__icontains=test_restaurant).exists():
                possible_restaurant1 = test_restaurant
            else:
                possible_dish1 = test_dish
                break


        query = Q()
        query1 = Q()

        # To decide which are the right combinations the words classified into
        if possible_dish and Dish.objects.filter(name__icontains=possible_dish).exists():
            query &= Q(name__icontains=possible_dish)
        if possible_restaurant and Restaurant.objects.filter(name__icontains=possible_restaurant).exists():
            query &= Q(restaurant__name__icontains=possible_restaurant)

        if possible_dish1 and Dish.objects.filter(name__icontains=possible_dish1).exists():
            query1 &= Q(name__icontains=possible_dish1)
        if possible_restaurant1 and Restaurant.objects.filter(name__icontains=possible_restaurant1).exists():
            query1 &= Q(restaurant__name__icontains=possible_restaurant1)
        
        if not query and query1:
            query = query1

        if price:
            query &= Q(price=price)

        results = results.filter(query)

        if veg_only:
            for keyword in non_veg_keywords:
                results = results.exclude(name__icontains=keyword)
    # Veg option
    elif veg_only:
        for keyword in non_veg_keywords:
            results = results.exclude(name__icontains=keyword)

    results_list = list(results)
    seen = set()
    unique_results = []

    # Allow lat n long to be passed down to leaflet.js
    for dish in results_list:
        if dish.name not in seen:
            unique_results.append(dish)
            seen.add(dish.name)
    for dish in unique_results:
        restaurant = dish.restaurant
        if restaurant.lat_long:
            lat, long = restaurant.lat_long.split(',')
            dish.lat = float(lat.strip())
            dish.long = float(long.strip())
        else:
            dish.lat = None
            dish.long = None
        dish.average_rating = round(restaurant.average_rating, 0)
        if dish.average_rating == 0:
            dish.average_rating = 1

    # To build with paginations
    paginator = Paginator(unique_results, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': original_query,
        'veg_only': veg_only
    }
    return render(request, 'search_app/search.html', context)
