from django.db import models
from django.contrib.auth import get_user_model
from places.models import Place
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()
RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)  
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.parent:
            return f"↳ پاسخ {self.user} به {self.parent.user}"
        return f"{self.user} روی {self.place.name}"




class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, related_name='ratings', on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="مقدار باید بین 1 تا 5 باشد"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'place')

    def __str__(self):
        return f"{self.value} ستاره برای {self.place.name} توسط {self.user.username}"



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, related_name='favorites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'place')

    def __str__(self):
        return f"{self.user} liked {self.place.name}"
