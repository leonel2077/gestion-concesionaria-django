from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    lenguage = models.CharField(max_length=30, choices= [
            ('en', ('English')),
            ('es', ('Español')),
    ],
    default='es'
    )