from django.core.management.base import BaseCommand
from quotes.models import Review
from datetime import datetime
import pytz

class Command(BaseCommand):
    help = 'Delete inappropriate reviews from July 4, 2025'

    def handle(self, *args, **options):
        # Define the date to filter by
        target_date = datetime(2025, 7, 4, tzinfo=pytz.UTC)
        
        # Find reviews from July 4, 2025 with inappropriate names
        inappropriate_names = ['Hairy Balls', 'Ben Dover']
        
        reviews_to_delete = Review.objects.filter(
            name__in=inappropriate_names,
            date_created__date=target_date.date()
        )
        
        print(f"Found {reviews_to_delete.count()} reviews to delete:")
        
        for review in reviews_to_delete:
            print(f"- ID: {review.id}, Name: '{review.name}', Comment: '{review.comment[:50]}...', Date: {review.date_created}")
        
        if reviews_to_delete.exists():
            # Ask for confirmation
            confirm = input("\nDo you want to delete these reviews? (yes/no): ")
            if confirm.lower() == 'yes':
                deleted_count = reviews_to_delete.count()
                reviews_to_delete.delete()
                print(f"\nSuccessfully deleted {deleted_count} inappropriate reviews.")
            else:
                print("Deletion cancelled.")
        else:
            print("No inappropriate reviews found to delete.")
