from django.core.management.base import BaseCommand
from quotes.models import Review
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete inappropriate reviews from July 4, 2025'

    def handle(self, *args, **options):
        # Define the date to filter by
        target_date = datetime(2025, 7, 4)
        
        # Find reviews from July 4, 2025 with inappropriate names
        inappropriate_names = ['Hairy Balls', 'Ben Dover']
        
        reviews_to_delete = Review.objects.filter(
            name__in=inappropriate_names,
            created_at__date=target_date.date()
        )
        
        print(f"Found {reviews_to_delete.count()} reviews to delete:")
        
        for review in reviews_to_delete:
            print(f"- ID: {review.id}, Name: '{review.name}', Comment: '{review.description[:50]}...', Date: {review.created_at}")
        
        if reviews_to_delete.exists():
            # Delete without confirmation in automated environment
            deleted_count = reviews_to_delete.count()
            reviews_to_delete.delete()
            print(f"\nSuccessfully deleted {deleted_count} inappropriate reviews.")
        else:
            print("No inappropriate reviews found to delete.")
