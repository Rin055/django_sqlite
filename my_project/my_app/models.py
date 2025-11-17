from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Order(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.product_name
