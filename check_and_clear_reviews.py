#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review

# Check current reviews
reviews = Review.objects.all()
print(f'=== PRODUCTION DATABASE STATUS ===')
print(f'Total reviews: {reviews.count()}')

if reviews.count() > 0:
    print('\nExisting reviews:')
    for i, review in enumerate(reviews, 1):
        print(f'{i}. Name: {review.name}')
        print(f'   Rating: {review.rating}')
        print(f'   Description: {review.description[:100]}...')
        print(f'   Created: {review.created_at}')
        print('-' * 50)
        
    # Clear all reviews
    print(f'\nDeleting all {reviews.count()} reviews...')
    Review.objects.all().delete()
    print('All reviews deleted!')
else:
    print('No reviews found in database.')

# Final verification
final_count = Review.objects.count()
print(f'\nFinal verification: {final_count} reviews remaining')
