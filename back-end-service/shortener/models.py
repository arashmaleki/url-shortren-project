from string import ascii_letters
from django.db import models
from random import choices
from django.conf import settings
from django.db.models import CASCADE
from users.models import User


class Shortener(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    short_url = models.URLField(blank=True, null=True, unique=True)
    long_url = models.URLField()
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def generate_short_url():
        while True:
            string_list = choices(ascii_letters + "".join([str(i) for i in range(10)]), k=6)
            random_string = "".join(string_list)
            new_link = settings.BASE_URL + random_string

            if not Shortener.objects.filter(short_url=new_link).exists():
                break
        return new_link

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        return super().save(*args, **kwargs)
