from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', default=1)
    
    def __str__(self):
        return f' This is Title: {self.title[0:20]} and author {self.author}'
    