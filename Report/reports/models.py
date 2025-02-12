from django.db import models

class Report(models.Model):
    title_number = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    inspection_date = models.DateField(default='2000-01-01')
    Cordinates = models.CharField(default=0, max_length=50)
    land_size = models.CharField(default=0, max_length=50)
    market_value = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    mortgage_value = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    forced_sale_value = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    reserve_value = models.DecimalField(default=0,  max_digits=15, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Report: {self.title_number}"
