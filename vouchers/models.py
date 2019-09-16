from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Voucher(models.Model):
    voucher_code = models.CharField(unique=True, max_length=30)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    active = models.BooleanField()

    def __str__(self):
        return self.form

