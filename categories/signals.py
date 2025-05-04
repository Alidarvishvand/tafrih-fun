from .models import Province
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_provinces(sender, **kwargs):
    provinces = [
        "آذربایجان شرقی", "آذربایجان غربی", "اردبیل", "اصفهان", "البرز", "ایلام", "بوشهر",
        "تهران", "چهارمحال و بختیاری", "خراسان جنوبی", "خراسان رضوی", "خراسان شمالی", "خوزستان",
        "زنجان", "سمنان", "سیستان و بلوچستان", "فارس", "قزوین", "قم", "کردستان", "کرمان",
        "کرمانشاه", "کهگیلویه و بویراحمد", "گلستان", "گیلان", "لرستان", "مازندران", "مرکزی",
        "هرمزگان", "همدان", "یزد"
    ]
    for name in provinces:
        Province.objects.get_or_create(name=name)
