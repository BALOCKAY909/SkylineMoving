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
    'name': 'Kimberly Kingston',
    'rating': 'none',  # No rating as requested
    'description': '''Skyline movers did a great job for us!  Angelo responded to our Nextdoor Neighbor message promptly.   I explained what we needed to move and where, they provided the price and gave their next opening.  When we agreed on a date and time, they showed up right on time!  We walked through what was needed and they got right to work.  We needed my grandmas bedroom furniture moved from a basement bedroom to a 2nd floor bedroom.  It was very heavy and it was very hot outside but they took all the needed precautions to protect the furniture and themselves!

They even moved a few things that my husband was going to take care of himself!

Through the heat and the work of moving everything, they remained pleasant and respectful!

We will definitely use them again if we need anything moved!  Highly recommend these two young men!''',
    'created_at': datetime(2025, 6, 15, 12, 0, 0, tzinfo=timezone.get_current_timezone())  # June 15, 2025
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
    print("\nAll reviews in database (newest first):")
    for i, r in enumerate(all_reviews, 1):
        print(f"{i}. {r.name} ({r.created_at.strftime('%B %d, %Y')})")
    
except Exception as e:
    print(f"❌ Error adding review: {e}")
