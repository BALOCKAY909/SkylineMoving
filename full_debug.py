#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review
from quotes.views import quote_request
from django.test import RequestFactory
from django.db.models import Case, When, IntegerField

print('=== TESTING PRODUCTION VIEW ===')

# Create a fake request
factory = RequestFactory()
request = factory.get('/')

# Get the reviews the same way the view does
all_reviews = Review.objects.annotate(
    rating_order=Case(
        When(rating='5', then=5),
        When(rating='4', then=4),
        When(rating='3', then=3),
        When(rating='2', then=2),
        When(rating='1', then=1),
        When(rating='none', then=0),
        output_field=IntegerField(),
    )
).order_by('-rating_order', '-created_at')

print(f'Total reviews from query: {all_reviews.count()}')
print(f'Reviews to display: {all_reviews[:4].count()}')

if all_reviews.count() > 0:
    print('\nReviews found:')
    for i, review in enumerate(all_reviews[:4], 1):
        print(f'{i}. {review.name} - {review.rating} stars')
        print(f'   "{review.description}"')
        print(f'   Created: {review.created_at}')
        print()
else:
    print('No reviews found in database query.')

# Clear the database completely
print('\n=== CLEARING DATABASE ===')
Review.objects.all().delete()
print('Database cleared.')

# Verify
final_count = Review.objects.count()
print(f'Final review count: {final_count}')

# Try to remove the SQLite file if it exists
import os
if os.path.exists('/app/db.sqlite3'):
    try:
        os.remove('/app/db.sqlite3')
        print('SQLite file removed')
    except Exception as e:
        print(f'Could not remove SQLite file: {e}')
else:
    print('SQLite file not found')
