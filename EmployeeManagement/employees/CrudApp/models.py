from django.db import models


# Create your models here.

class Employees(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)
    Address = models.TextField()
    Phone_Number = models.IntegerField()

    def __str__(self):
        return self.Name
