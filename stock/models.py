from django.db import models
from django.db.models import Model


# Create your models here.
class Battery(Model):
    model_no = models.CharField(max_length=150, unique=True)
    stock = models.PositiveIntegerField()
    code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model_no} | Stock: {self.stock}"

    class Meta:
        verbose_name_plural = 'Batteries'


class Keyboard(Model):
    model_no = models.CharField(max_length=150, unique=True)
    stock = models.PositiveIntegerField()
    code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model_no} | Stock: {self.stock}"


class Laptop(Model):
    name = models.CharField(max_length=150, unique=True)
    battery = models.ForeignKey(blank=True, null=True, on_delete=models.RESTRICT, to=Battery)
    keyboard = models.ForeignKey(blank=True, null=True, on_delete=models.RESTRICT, to=Keyboard)

    def __str__(self):
        return f"{self.name}"