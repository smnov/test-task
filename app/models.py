from django.db import models
from datetime import datetime

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=500)
    char_count = models.IntegerField(max)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
