from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

# id, name, username,password
class User(AbstractUser):
    # id = models.IntegerField(primary_key=True, unique=True, null=False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table= 'user'