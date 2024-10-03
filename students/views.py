from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()  # Retrieve all students
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)  # Get student by ID
    return render(request, 'students/student_detail.html', {'student': student})

def add_student(request):
    # Logic to add a new student will go here
    pass

def edit_student(request, student_id):
    # Logic to edit student information
    pass

