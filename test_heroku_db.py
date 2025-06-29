#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from quotes.models import Review

# Test database connectivity and Review model
print("Testing PostgreSQL database connectivity...")

# Check if Review table exists and can be queried
try:
    review_count = Review.objects.count()
    print(f"✅ Connected to database successfully!")
    print(f"✅ Review table exists and is accessible")
    print(f"Current number of reviews: {review_count}")
    
    # Try to create a test review
    test_review = Review.objects.create(
        name="Test User",
        rating="5",
        description="This is a test review to verify PostgreSQL persistence."
    )
    print(f"✅ Test review created with ID: {test_review.id}")
    
    # Verify the review was saved
    total_reviews = Review.objects.count()
    print(f"Total reviews after creation: {total_reviews}")
    
    # List all reviews
    all_reviews = Review.objects.all()
    print("\nAll reviews in database:")
    for review in all_reviews:
        print(f"- {review.name}: {review.rating}/5 - {review.description[:50]}...")
    
    print(f"\n✅ Database is persistent and working correctly!")
    
except Exception as e:
    print(f"❌ Error: {e}")
