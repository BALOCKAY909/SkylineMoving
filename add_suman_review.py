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
    'name': 'Suman Kantheti',
    'rating': 'none',  # No rating as requested
    'description': '''Reached out to every branded movers in
Omaha and got only exorbitant quotes. And then found Angelo and Brady (Skyline moving) .. was skeptical but went ahead with a hunch. 

And they arrived on dot  the time they had discussed and then from that point they surprised me Every minute. The attention to the  needs, the care which they took of every item and asked specifically where each item needs to go in the  new location.  And they very courteous. 

i wish all the success !!

Reasonably Priced and very very  professional.''',
    'created_at': datetime(2025, 5, 26, 12, 0, 0, tzinfo=timezone.get_current_timezone())  # May 26, 2025
}

try:
    # Create the review
    review = Review.objects.create(**review_data)
    print(f"✅ Review successfully added!")
    print(f"   ID: {review.id}")
    print(f"   Name: {review.name}")
    print(f"   Rating: {review.rating}")
    print(f"   Date: {review.created_at}")
    print(f"   Review: {review.description[:100]}...")
    
    # Verify total count
    total_reviews = Review.objects.count()
    print(f"\nTotal reviews in database: {total_reviews}")
    
    # List all reviews to verify order
    all_reviews = Review.objects.all().order_by('-created_at')
    print("\nAll reviews in database:")
    for i, r in enumerate(all_reviews, 1):
        print(f"{i}. {r.name} ({r.created_at.strftime('%B %d, %Y')})")
    
except Exception as e:
    print(f"❌ Error adding review: {e}")
