from django.db import models
from rest_framework import serializers

from staff.models import Staff

# Create your models here.

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = (
            'id',
            'name',
            'nip',
            'phone',
            'email',
            'role',
            'address'
        )