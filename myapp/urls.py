from django.contrib import admin
from django.urls import path
from .views import employeeListView , employeeDetailView ,  UserListView

urlpatterns = [
   # path('admin/' , admin.site.urls),
    path('employees/', employeeListView),
    path('employees/<int:pk>/',employeeDetailView),
    path('users/', UserListView),
    
]