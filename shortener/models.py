from django.db import models
import random
import string

class Link(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choices(characters, k=6))
            if not Link.objects.filter(short_code=short_code).exists():
                return short_code

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
