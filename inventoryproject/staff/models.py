from django.db import models


# Create your models here.

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    nip = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table= 'staffs'