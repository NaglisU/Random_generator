# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name