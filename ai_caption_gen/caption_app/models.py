from django.db import models


class CaptionModel(models.Model):
    image = models.ImageField(upload_to='captions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)