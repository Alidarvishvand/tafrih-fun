from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    # province = models.ForeignKey(Province, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name







class Media(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='media/')

    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='media')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='media')

    def __str__(self):
        return f"{self.media_type} for {self.province.name} - {self.subcategory.name}"