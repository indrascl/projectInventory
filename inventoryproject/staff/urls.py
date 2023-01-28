from django.urls import path
from staff import views

urlpatterns = [
    path('staff', views.StaffList.as_view()),
    path('staff/<id>', views.StaffDetail.as_view())
]