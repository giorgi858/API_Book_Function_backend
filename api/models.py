from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f' This is Title: {self.title[0:20]}'
    