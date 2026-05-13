from django.db import models

# Create your models here.

class Contact(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]


    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name