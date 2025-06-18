#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
import django
django.setup()

from quotes.models import Review

# Create a test review to verify the fix
review = Review.objects.create(
    name='',  # Empty name should be handled by the model default
    rating='5',
    description='Test review to verify name field displays Anonymous when empty'
)

print(f'Test review created:')
print(f'Name: "{review.name}"')
print(f'Rating: {review.rating}')
print(f'Description: {review.description}')
