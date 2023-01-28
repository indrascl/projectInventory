from django.http import JsonResponse
from rest_framework.views import APIView
from inventory.models import Inventories

from inventory.serializer import InventoriesSerializer, InventoriesShowSerializer

from rest_framework.permissions import IsAuthenticated

class InventoriesList(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        inventoriesObj = Inventories.objects.all()
        
        inventoriesSerializer = InventoriesShowSerializer(inventoriesObj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": inventoriesSerializer.data,
            "message": "Get data successfully"
        })
        
        
    def post(self, request):
        
        body = request.data 
      
        
        inventorySerializer = InventoriesSerializer(data={
            "unitName": body['unitName'],
            "quantity": body['quantity'],
            "unitCode": body['unitCode'],
            "type": body['type'],
            "purchasePrice": body['purchasePrice'],
            "purchaseYear": body['purchaseYear'],
            "category": body['category_id'],
        })
        
        if inventorySerializer.is_valid():
            inventorySerializer.save()
            
            return JsonResponse({
              "error": False,
              "data": inventorySerializer.data,
              "message": "Data saved successfully"
            })
            
        else:
            
            return JsonResponse({
                "error": True,
                "data": None,
                "message": inventorySerializer.errors
            })


class InventoryDetail(APIView):
    
    def get(self, request, id):
        
        inventoryObj = Inventories.objects.filter(id=id).first()
        
        inventorySerializer = InventoriesShowSerializer(inventoryObj)
        
        return JsonResponse({
            "error": False,
            "data": inventorySerializer.data
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        inventoryObj = Inventories.objects.filter(id=id).first()
        
        inventorySerializer = InventoriesSerializer(inventoryObj, data={
            "unitName": body['unitName'],
            "quantity": body['quantity'],
            "unitCode": body['unitCode'],
            "type": body['type'],
            "purchasePrice": body['purchasePrice'],
            "purchaseYear": body['purchaseYear'],
            "category": body['category_id'],

        })
        
        if inventorySerializer.is_valid():
            inventorySerializer.save()
            
            return JsonResponse({
                "error": False,
                "data": inventorySerializer.data,
                "message": "Data updated successfully"
            })
        
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message": inventorySerializer.errors
            })
            
    def delete(self, request, id):
        
        inventoryObject = Inventories.objects.filter(id=id)
        
        inventoryObject.delete()
        
        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })