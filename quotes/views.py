from django.shortcuts import render, redirect
from .forms import QuoteRequestForm, ReviewForm
from .models import Review
from django.core.mail import send_mail
from django.http import JsonResponse
import json

# Create your views here.

def quote_request(request):
    success = False
    review_success = False
    
    if request.method == 'POST':
        # Check if it's a review submission
        if 'description' in request.POST or 'rating' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                # Save review to database
                Review.objects.create(
                    name=review_form.cleaned_data['name'],
                    rating=review_form.cleaned_data['rating'],
                    description=review_form.cleaned_data['description']
                )
                review_success = True
                review_form = ReviewForm()  # Reset form
            form = QuoteRequestForm()  # Keep quote form as is
        else:
            # Handle quote request
            form = QuoteRequestForm(request.POST)
            if form.is_valid():
                # Prepare email content
                subject = 'New Quote Request from Skyline Moving'
                message = (
                    f"First Name: {form.cleaned_data['first_name']}\n"
                    f"Last Name: {form.cleaned_data['last_name']}\n"
                    f"Email: {form.cleaned_data['email']}\n"
                    f"Phone: {form.cleaned_data['phone']}\n"
                    f"Job Description: {form.cleaned_data['job_description']}\n"
                )
                send_mail(
                    subject,
                    message,
                    'skyline.moving.gp@gmail.com',  # From email
                    ['skyline.moving.gp@gmail.com'],  # To email
                    fail_silently=False,
                )
                success = True
                form = QuoteRequestForm()  # Reset form
            review_form = ReviewForm()  # Keep review form as is
    else:
        form = QuoteRequestForm()
        review_form = ReviewForm()
    
    all_reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'quotes/quote_form.html', {
        'form': form, 
        'review_form': review_form,
        'success': success,
        'review_success': review_success,
        'reviews': all_reviews[:4],  # Show latest 4 reviews
        'total_reviews_count': all_reviews.count()  # Pass total count
    })

def thank_you(request):
    return render(request, 'quotes/thank_you.html')

def all_reviews(request):
    """Display all reviews on a dedicated page"""
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'quotes/all_reviews.html', {
        'reviews': reviews
    })
