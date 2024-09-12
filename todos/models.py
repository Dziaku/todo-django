from django.db import models
from django.utils import timezone

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=256)
    deadline_date = models.DateTimeField()
    status = models.BooleanField(default= False)

    def __str__(self):
        return self.item_description