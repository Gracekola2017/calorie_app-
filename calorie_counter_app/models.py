from django.db import models

# Create your models here.

from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calorie_count = models.IntegerField()

    def __str__(self):
        return self.name



