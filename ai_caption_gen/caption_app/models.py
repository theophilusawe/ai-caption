from django.db import models
from django.core.files.storage import default_storage


class User(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, auto_created=True, )
    name = models.CharField(max_length=20, blank=False)


class CaptionModel(models.Model):
    image = models.ImageField(upload_to='captions/', storage=default_storage)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)