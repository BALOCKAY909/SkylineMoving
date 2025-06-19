#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review

# Clear all reviews
reviews = Review.objects.all()
count = reviews.count()
print(f'Found {count} reviews to delete')

if count > 0:
    Review.objects.all().delete()
    print(f'Deleted {count} reviews')
else:
    print('No reviews found')

# Verify
remaining = Review.objects.count()
print(f'Reviews remaining: {remaining}')
