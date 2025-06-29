#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review
from django.conf import settings

print('=== REVIEW DATABASE INVESTIGATION ===')
print(f'Database engine: {settings.DATABASES["default"]["ENGINE"]}')
print(f'Database name: {settings.DATABASES["default"]["NAME"]}')

# Check current reviews
reviews = Review.objects.all()
print(f'Total reviews in database: {reviews.count()}')

if reviews.count() > 0:
    print('\nExisting reviews:')
    for i, review in enumerate(reviews, 1):
        print(f'{i}. {review.name} - {review.rating} stars')
        print(f'   "{review.description}"')
        print(f'   Created: {review.created_at}')
else:
    print('No reviews found in database.')

# Test creating a review
print('\n=== TESTING REVIEW CREATION ===')
try:
    test_review = Review.objects.create(
        name='Test Review User',
        rating='5',
        description='This is a test review to verify database persistence'
    )
    print(f'Successfully created test review: {test_review}')
    
    # Verify it was saved
    saved_reviews = Review.objects.all()
    print(f'Reviews after creation: {saved_reviews.count()}')
    
    # Delete the test review
    test_review.delete()
    print('Test review deleted.')
    
except Exception as e:
    print(f'Error creating review: {e}')

print('\n=== DATABASE TABLE STRUCTURE ===')
try:
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='quotes_review';")
    result = cursor.fetchone()
    if result:
        print('Review table structure:')
        print(result[0])
    else:
        print('Review table not found!')
except Exception as e:
    print(f'Error checking table structure: {e}')
