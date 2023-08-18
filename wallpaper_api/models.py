from django.db import models

class Image(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.ImageField(null=True, blank=True)