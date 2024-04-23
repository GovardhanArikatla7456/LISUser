from django.db import models

# Create your models here.
# user model with required fields in it.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
