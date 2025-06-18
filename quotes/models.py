from django.db import models
from django.utils import timezone

# Create your models here.

class Review(models.Model):
    STAR_CHOICES = [
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
        ('none', 'No Rating'),
    ]
    
    name = models.CharField(max_length=100, default='Anonymous')
    rating = models.CharField(max_length=4, choices=STAR_CHOICES, default='none')
    description = models.TextField(default='none')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.rating} stars"
    
    class Meta:
        ordering = ['-created_at']  # Most recent first
