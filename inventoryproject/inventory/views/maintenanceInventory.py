from django.http import JsonResponse
from rest_framework.views import APIView

from inventory.models import MaintenanceInventories
from staff.models import Staff

from inventory.serializer import MaintenanceInventoriesSerializer, MaintenanceInventoriesShowSerializer, StaffDetailSerializer
from staff.serializer import StaffSerializer

from rest_framework.permissions import IsAuthenticated

class MaintenanceInventoriesList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        maintenanceInventoriesObj = MaintenanceInventories.objects.all()
        
        maintenanceInventoriesSerializer = MaintenanceInventoriesShowSerializer(maintenanceInventoriesObj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": maintenanceInventoriesSerializer.data,
            "message": "Get data successfully"
        })
        
        
    def post(self, request):
        
        body = request.data 
      
        
        maintenanceInventorySerializer = MaintenanceInventoriesSerializer(data={
            "id": body['id'],
            "maintenanceDate": body['maintenanceDate'],
            "maintenanceVendor": body['maintenanceVendor'],
            "inventory": body['inventory_id'],
            "staff": body['staff_id'],
        })
        
        if maintenanceInventorySerializer.is_valid():
            maintenanceInventorySerializer.save()
            
            return JsonResponse({
              "error": False,
              "data": maintenanceInventorySerializer.data,
              "message": "Data saved successfully"
            })
            
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": maintenanceInventorySerializer.errors
            })


class MaintenanceInventoryDetail(APIView):
    
    def get(self, request, id):
        
        maintenanceInventoryObj = MaintenanceInventories.objects.filter(id=id).first()
        
        maintenanceInventorySerializer = MaintenanceInventoriesShowSerializer(maintenanceInventoryObj)
        
        return JsonResponse({
            "error": False,
            "data": maintenanceInventorySerializer.data
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        maintenanceInventoryObj = MaintenanceInventories.objects.filter(id=id).first()
        
        maintenanceInventorySerializer = MaintenanceInventoriesSerializer(maintenanceInventoryObj, data={
           "id": body['id'],
            "maintenanceDate": body['maintenanceDate'],
            "maintenanceVendor": body['maintenanceVendor'],
            "inventory": body['inventory_id'],
            "staff": body['staff_id'],
        })
        
        if maintenanceInventorySerializer.is_valid():
            maintenanceInventorySerializer.save()
            
            return JsonResponse({
                "error": False,
                "data":  maintenanceInventorySerializer.data,
                "message": "Data updated successfully"
            })
        
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message":  maintenanceInventorySerializer.errors
            })
            
    def delete(self, request, id):
        
        maintenanceInventoryObject = MaintenanceInventories.objects.filter(id=id)
        
        maintenanceInventoryObject.delete()
        
        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })

class StaffDetailAPIView(APIView):
    def get(self, request, id):

        staffDetail = Staff.objects.filter(id=id).first()
        staffDetailSerializer = StaffDetailSerializer(staffDetail)


        return JsonResponse({
            "error": False,
            "data": staffDetailSerializer.data
        })