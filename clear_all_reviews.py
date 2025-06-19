#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review

# Check and clear all reviews
count = Review.objects.count()
print(f'Found {count} reviews in database')

if count > 0:
    Review.objects.all().delete()
    print(f'Successfully deleted {count} reviews')
else:
    print('No reviews to delete')

# Final verification
final_count = Review.objects.count()
print(f'Final count: {final_count} reviews remaining')
