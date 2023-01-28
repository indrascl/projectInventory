from django.http import JsonResponse
from rest_framework.views import APIView
from inventory.models import Category

from inventory.serializer import CategorySerializer

from rest_framework.permissions import IsAuthenticated

class CategoryList(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        categoryObj = Category.objects.all()
        
        categorySerializer = CategorySerializer(categoryObj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": categorySerializer.data,
            "message": "Get data successfully"
        })
        
        
    def post(self, request):
        
        body = request.data 
      
        
        categorySerializer = CategorySerializer(data={
            "id": body['id'],
            "name": body['name']
           
        })
        
        if categorySerializer.is_valid():
            categorySerializer.save()
            
            return JsonResponse({
              "error": False,
              "data": categorySerializer.data,
              "message": "Data saved successfully"
            })
            
        else:
            
            return JsonResponse({
                "error": True,
                "data": None,
                "message": categorySerializer.errors
            })


class CategoryDetail(APIView):
    
    def get(self, request, id):
        
        categoryObj = Category.objects.filter(id=id).first()
        
        categorySerializer = CategorySerializer(categoryObj)
        
        return JsonResponse({
            "error": False,
            "data": categorySerializer.data
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        categoryObj = Category.objects.filter(id=id).first()
        
        categorySerializer = CategorySerializer(categoryObj, data={
            "id": body['id'],
            "name": body['name']
        })
        
        if categorySerializer.is_valid():
            categorySerializer.save()
            
            return JsonResponse({
                "error": False,
                "data": categorySerializer.data,
                "message": "Data updated successfully"
            })
        
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message": categorySerializer.errors
            })
            
    def delete(self, request, id):
        
        categoryObject = Category.objects.filter(id=id)
        
        categoryObject.delete()
        
        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })