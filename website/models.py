from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=250)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.TextField()
    Description = models.TextField()

    def __str__(self):
        return self.Name