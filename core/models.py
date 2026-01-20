from django.db import models
from datetime import date
from cloudinary.models import CloudinaryField


class Enrollment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.TextField()
    enrollment_date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(editable=False, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def calculate_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super().save(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover_image = CloudinaryField('image')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Gallery(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.album.title})"