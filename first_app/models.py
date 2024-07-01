from django.db import models
from django.utils.text import slugify
from datetime import timedelta , date

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    phone_no = models.CharField(max_length=11)
    # slug = models.SlugField(max_length=200, unique=True)
    # auto_field = models.AutoField(primary_key=True,null=False)
    FAVORITE_FOOD_CHOICES = [
        ('pasta', 'pasta'),
        ('udon', 'udon'),
        ('pizza', 'pizza'),
    ]
    favorite_food = models.CharField(max_length=20, choices=FAVORITE_FOOD_CHOICES, default='pasta')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Generate the slug from the name if not provided
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Doctor - {self.name}'
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    problem = models.TextField()
    health_condition = models.TextField()
    phone_no = models.CharField(max_length=11)

    def __str__(self):
        return f'Patient - {self.name}'
    