from django.db import models
from staff.models import Staff
from datetime import date

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'categories'


class Inventories(models.Model):
    id = models.AutoField(primary_key=True)
    unitName = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField()
    unitCode = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=False, blank=False)
    purchasePrice= models.IntegerField()
    purchaseYear = models.CharField(max_length=11, null=False, blank=False)
    
    class Meta:
        db_table = 'inventories'


class MaintenanceInventories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    inventory = models.ForeignKey(Inventories, on_delete=models.CASCADE, related_name="relasi_inventory")
    maintenanceDate = models.DateField()
    maintenanceVendor = models.CharField(max_length=100, null=False, blank=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="relasi_staff")
    
    class Meta:
        db_table= 'maintenance_inventories'