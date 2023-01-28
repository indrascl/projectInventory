from rest_framework import serializers

from datetime import date

from staff.serializer import StaffSerializer
from staff.models import Staff

from inventory.models import Category, Inventories, MaintenanceInventories
     
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class InventoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventories
        fields = (
            'id',
            'unitName',
            'quantity',
            'unitCode',
            'type',
            'purchasePrice',
            'purchaseYear',
            'category'
        )

class InventoriesShowSerializer(serializers.ModelSerializer):
     
    category = CategorySerializer()
    
    class Meta:
        model = Inventories
        fields = (
            'id',
            'unitName',
            'quantity',
            'unitCode',
            'type',
            'purchasePrice',
            'purchaseYear',
            'category'
        )


class MaintenanceInventoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceInventories
        fields = (
            'id',
            'maintenanceDate',
            'maintenanceVendor',
            'inventory',
            'staff'
        )

class MaintenanceInventoriesShowSerializer(serializers.ModelSerializer):
     
    inventory = InventoriesSerializer()
    staff = StaffSerializer()
    
    class Meta:
        model = MaintenanceInventories
        fields = (
           'id',
            'maintenanceDate',
            'maintenanceVendor',
            'inventory',
            'staff'
        )


class MaintenanceHistorySerializer(serializers.ModelSerializer):
     
    inventory = InventoriesSerializer()
    
    class Meta:
        model = MaintenanceInventories
        fields = (
           'id',
            'maintenanceDate',
            'maintenanceVendor',
            'inventory'
        )

class StaffDetailSerializer(serializers.ModelSerializer):
    maintenanceInventories = MaintenanceHistorySerializer(many=True, source='relasi_staff')

    class Meta:
        model = Staff
        fields = (
            'id',
            'name',
            'maintenanceInventories'
        )