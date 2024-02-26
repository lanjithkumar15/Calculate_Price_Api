from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non-perishable', 'Non-Perishable')
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.description

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=50)
    base_distance_in_km = models.DecimalField(max_digits=5, decimal_places=2)
    km_price = models.DecimalField(max_digits=5, decimal_places=2)
    fix_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Pricing for {self.organization.name} - {self.item.description} - {self.zone}"
