from django.db import models

# Create your models here.

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    body = models.TextField()
