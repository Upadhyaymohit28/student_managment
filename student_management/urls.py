from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for admin panel
    path('students/', include('students.urls')),  # Include the students app URLs
    path('', include('students.urls')),  # Include students URLs for the root URL
]
