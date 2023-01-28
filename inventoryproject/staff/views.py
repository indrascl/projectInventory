from django.http import JsonResponse
from rest_framework.views import APIView

from staff.models import Staff
from staff.serializer import StaffSerializer

from rest_framework.permissions import IsAuthenticated

class StaffList(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        staffObj = Staff.objects
        
        staffSerializer = StaffSerializer(staffObj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": staffSerializer.data,
            "message": "Get data successfully"
        })

    def post(self, request):
        
        body = request.data 
        
        staffSerializer = StaffSerializer(data={
            "name": body['name'],
            "nip": body['nip'],
            "phone": body['phone'],
            "email": body['email'],
            "role": body['role'],
            "address": body['address']

        })
        
        if staffSerializer.is_valid():

            staffSerializer.save()
            
            return JsonResponse({
              "error": False,
              "data": staffSerializer.data,
              "message": "Data saved successfully"
            })
            
        else:
            
            return JsonResponse({
                "error": True,
                "data": None,
                "message": staffSerializer.errors
            })

class StaffDetail(APIView):
    
    def get(self, request, id):
        
        staffObj = Staff.objects.filter(id=id).first()
        
        staffSerializer = StaffSerializer(staffObj)
        
        return JsonResponse({
            "error": False,
            "data": staffSerializer.data
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        staffObj = Staff.objects.filter(id=id).first()
        
        staffSerializer = StaffSerializer(staffObj, data={
            "name": body['name'],
            "nip": body['nip'],
            "phone": body['phone'],
            "email": body['email'],
            "role": body['role'],
            "address": body['address']
        })
        
        if staffSerializer.is_valid():
            staffSerializer.save()
            
            return JsonResponse({
                "error": False,
                "data": staffSerializer.data,
                "message": "Data updated successfully"
            })
        
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message": staffSerializer.errors
            })
            
    def delete(self, request, id):
        
        staffObject = Staff.objects.filter(id=id)
        
        staffObject.delete()
        
        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })