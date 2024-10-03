from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Maps to the student list view
    path('<int:student_id>/', views.student_detail, name='student_detail'),  # Maps to student detail view
    path('add/', views.add_student, name='add_student'),  # Maps to add student view
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),  # Maps to edit student view
]
# Custom error handlers
handler404 = 'students.views.custom_404'
handler500 = 'students.views.custom_500'