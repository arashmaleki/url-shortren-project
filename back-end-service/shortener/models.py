from string import ascii_letters
from django.db import models
from random import choices
from django.db.models import CASCADE
from users.models import User
from django.core.validators import URLValidator


class Shortener(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    short_url = models.CharField(unique=True, max_length=500, blank=True)
    long_url = models.TextField(validators=[URLValidator()])
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def generate_short_url():
        while True:
            string_list = choices(ascii_letters + "".join([str(i) for i in range(10)]), k=6)
            new_link = "".join(string_list)
            if not Shortener.objects.filter(short_url=new_link).exists():
                break
        return new_link

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        return super().save(*args, **kwargs)
