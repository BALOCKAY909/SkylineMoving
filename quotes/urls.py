from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote_request, name='quote_request'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('all-reviews/', views.all_reviews, name='all_reviews'),
    path('services/', views.services, name='services'),
    path('areas-served/', views.areas_served, name='areas_served'),
    path('verifyreviews/', views.review_login, name='review_login'),
    path('verify-reviews/', views.verify_reviews, name='verify_reviews'),
    path('review-logout/', views.review_logout, name='review_logout'),
]