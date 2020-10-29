from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("title", max_length=256)
    text = models.TextField("text")
    preview_text = models.TextField('preview-text')