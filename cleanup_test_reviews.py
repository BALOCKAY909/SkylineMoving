#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review

# Delete all test reviews
Review.objects.all().delete()
print("All test reviews deleted")
print(f"Current review count: {Review.objects.count()}")
