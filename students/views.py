from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def add_student(request):
    # View code here
    pass

@login_required
def edit_student(request, student_id):
    # View code here
    pass


# View to display the list of students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# View to display details of a single student
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

# View to add a new student using the StudentForm
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list page after saving
    else:
        form = StudentForm()  # If the request is GET, render an empty form
    return render(request, 'students/add_student.html', {'form': form})

# View to edit an existing student's information using the StudentForm
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # Bind form to existing student instance
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)  # Redirect to the updated student's detail page
    else:
        form = StudentForm(instance=student)  # Render form pre-filled with student's information
    return render(request, 'students/edit_student.html', {'form': form})
