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
    'name': 'Baillie Strong Olsen',
    'rating': 'none',  # No rating as requested
    'description': 'They did a great job helping us load some stuff in our u-haul!',
    'created_at': datetime(2025, 6, 18, 12, 0, 0, tzinfo=timezone.get_current_timezone())  # June 18, 2025
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
    
    # List all reviews to verify order
    all_reviews = Review.objects.all().order_by('-created_at')
    print("\nAll reviews in database (newest first):")
    for i, r in enumerate(all_reviews, 1):
        print(f"{i}. {r.name} ({r.created_at.strftime('%B %d, %Y')})")
    
except Exception as e:
    print(f"❌ Error adding review: {e}")
