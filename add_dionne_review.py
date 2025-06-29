#!/usr/bin/env python
import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review
from django.utils import timezone

# Create the specific review
review_data = {
    'name': 'Dionne Finken',
    'rating': 'none',  # No rating as requested
    'description': 'I used skyline moving on Friday as I had an unexpected need for some items in our storage unit. Last minute booking and they were able to accommodate. Very affordable pricing, efficient, and on time.  I will definitely recommend these 2 college students.',
    'created_at': datetime(2025, 6, 1, 12, 0, 0, tzinfo=timezone.get_current_timezone())  # June 1, 2025
}

try:
    # Create the review
    review = Review.objects.create(**review_data)
    print(f"✅ Review successfully added!")
    print(f"   ID: {review.id}")
    print(f"   Name: {review.name}")
    print(f"   Rating: {review.rating}")
    print(f"   Date: {review.created_at}")
    print(f"   Review: {review.description}")
    
    # Verify total count
    total_reviews = Review.objects.count()
    print(f"\nTotal reviews in database: {total_reviews}")
    
except Exception as e:
    print(f"❌ Error adding review: {e}")
