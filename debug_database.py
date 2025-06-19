#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from django.conf import settings
from quotes.models import Review

print('=== DATABASE CONFIGURATION ===')
print(f"Database ENGINE: {settings.DATABASES['default']['ENGINE']}")
print(f"Database NAME: {settings.DATABASES['default']['NAME']}")
print(f"Database HOST: {settings.DATABASES['default'].get('HOST', 'N/A')}")
print(f"Database PORT: {settings.DATABASES['default'].get('PORT', 'N/A')}")

print('\n=== REVIEWS IN DATABASE ===')
reviews = Review.objects.all()
print(f'Total reviews: {reviews.count()}')

if reviews.count() > 0:
    for i, review in enumerate(reviews, 1):
        print(f'{i}. {review.name} - {review.rating} stars')
        print(f'   "{review.description[:100]}..."')
        print(f'   Created: {review.created_at}')
        print()
        
    # Delete all reviews
    print('DELETING ALL REVIEWS...')
    Review.objects.all().delete()
    print('All reviews deleted!')
    
    # Verify deletion
    final_count = Review.objects.count()
    print(f'Reviews remaining: {final_count}')
else:
    print('No reviews found.')
