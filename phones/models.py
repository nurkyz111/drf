from django.db import models


class Phone(models.Model):
    COLOR_CHOICES = (
        ('GREY', 'Grey'),
        ('RED', 'Red'),
        ('BLACK', 'Black'),
        ('PURPLE', 'Purple')
    )
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(choices=COLOR_CHOICES, max_length=6)

    def __str__(self):
        return f'{self.name} - {self.model}'

