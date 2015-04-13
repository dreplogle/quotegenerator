from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    
