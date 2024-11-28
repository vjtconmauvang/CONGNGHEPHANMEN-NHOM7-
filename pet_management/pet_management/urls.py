# pet_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pets.urls')),  # Thêm dòng này để bao gồm URLs của ứng dụng pets
]
