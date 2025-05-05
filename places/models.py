from django.db import models
from categories.models import Province, SubCategory


class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)  
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.province.name} - {self.subcategory.name})"


class PlaceMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    place = models.ForeignKey('Place', related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='place_media/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type} for {self.place.name}"
