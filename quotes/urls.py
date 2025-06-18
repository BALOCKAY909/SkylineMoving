from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote_request, name='quote_request'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('all-reviews/', views.all_reviews, name='all_reviews'),
] 