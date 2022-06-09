from django.db import models


class Category(models.Model):
    CAR_TYPE = (
        ('Passenger', 'Passenger'),
        ('Cargo', 'Cargo'),
        ('Electo', 'Electro')
    )
    car_type = models.CharField(max_length=30, choices=CAR_TYPE)
    description = models.TextField()

    def __str__(self):
        return self.car_type


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='car')
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.model
