from django.db import models

# Create your models here.
class Todo(models.Model):
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=100)
    Date_Of_Birth = models.DateField()
