from django.db import models
import uuid

def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.ImageField(upload_to=upload_to, null=True, blank=True)