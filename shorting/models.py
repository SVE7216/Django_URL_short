from django.db import models
from django.contrib.auth.models import User


class URLModels(models.Model):
    origin_url = models.URLField()
    short_id = models.SlugField(max_length=8, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ['-date']

    def __str__(self):
        return f"{self.origin_url} - {self.short_id}"


