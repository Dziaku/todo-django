from django.db import models
from django.utils import timezone

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    task = models.CharField(max_length=256)
    deadline_date = models.DateTimeField()
    status = models.BooleanField(default= False)

    def __str__(self):
        return self.task