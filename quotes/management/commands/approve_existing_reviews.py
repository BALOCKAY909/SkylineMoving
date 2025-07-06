from django.core.management.base import BaseCommand
from quotes.models import Review

class Command(BaseCommand):
    help = 'Mark all existing reviews as approved'

    def handle(self, *args, **options):
        # Update all existing reviews to approved status
        updated_count = Review.objects.filter(approval_status='pending').update(approval_status='approved')
        
        print(f'Updated {updated_count} reviews to approved status.')
        
        # Show stats
        total_reviews = Review.objects.count()
        approved_reviews = Review.objects.filter(approval_status='approved').count()
        pending_reviews = Review.objects.filter(approval_status='pending').count()
        rejected_reviews = Review.objects.filter(approval_status='rejected').count()
        
        print(f'Total reviews: {total_reviews}')
        print(f'Approved: {approved_reviews}')
        print(f'Pending: {pending_reviews}')
        print(f'Rejected: {rejected_reviews}')
