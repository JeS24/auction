from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    """A model representing a product that goes up for auction"""

    def __str__(self):
        return self.name

    def is_live(self):
        return (self.start_time < datetime.now) and (datetime.now < self.end_time)

    class Meta:
        ordering = ['end_time', 'start_time', 'name']

    name = models.CharField(max_length=100, verbose_name='Name of the Product')
    description = models.TextField(max_length=200)
    base_bid = models.DecimalField(decimal_places=2, max_digits=10)

    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)

    sold_status = models.BooleanField(default=False, editable=False)

    #seller = models.ForeignKey('User', on_delete=models.SET_NULL)
    #sold_to = models.ForeignKey('User', on_delete=models.SET_NULL)
