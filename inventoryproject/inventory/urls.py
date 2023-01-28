from django.urls import path

from inventory import views

urlpatterns = [
    path('category', views.category.CategoryList.as_view()),
    path('category/<id>', views.category.CategoryDetail.as_view()),
    
    path('inventories', views.inventories.InventoriesList.as_view()),
    path('inventories/<id>', views.inventories.InventoryDetail.as_view()),
  
    path('maintenanceInventories', views.maintenanceInventory.MaintenanceInventoriesList.as_view()),
    path('maintenanceInventories/<id>', views.maintenanceInventory.MaintenanceInventoryDetail.as_view()),

    path('relasi/<id>', views.maintenanceInventory.StaffDetailAPIView.as_view())

   # path('stf/<id>', views.maintenanceInventory.StaffDetailAPIView.as_view())
  
]