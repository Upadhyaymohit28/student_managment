from django.shortcuts import render, get_object_or_404, redirect
from .models import Student  # Import the Student model
from .forms import StudentForm  # Import the StudentForm
from django.core.paginator import Paginator  # Import Paginator for pagination

# View to display the list of students with search and pagination functionality
def student_list(request):
    query = request.GET.get('q')  # Get the search term from the request

    # If a search term is entered, filter students by first name or last name
    if query:
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    else:
        students = Student.objects.all()  # If no search term, show all students

    # Implement pagination: Show 10 students per page
    paginator = Paginator(students, 10)  # Create a Paginator object
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the students for the current page

    # Render the template with the student data and page object
    return render(request, 'students/student_list.html', {'page_obj': page_obj, 'query': query})

# View to display details of a single student
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)  # Retrieve student by ID or return 404 if not found
    return render(request, 'students/student_detail.html', {'student': student})

# View to add a new student using the StudentForm
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  # Bind form with POST data
        if form.is_valid():  # Check if form is valid
            form.save()  # Save the new student to the database
            return redirect('student_list')  # Redirect to student list page after saving
    else:
        form = StudentForm()  # If the request is GET, render an empty form
    return render(request, 'students/add_student.html', {'form': form})

# View to edit an existing student's information using the StudentForm
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)  # Retrieve student by ID or return 404 if not found
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # Bind form to existing student instance
        if form.is_valid():
            form.save()  # Save the updated student information
            return redirect('student_detail', student_id=student.id)  # Redirect to updated student's detail page
    else:
        form = StudentForm(instance=student)  # Render form pre-filled with student's information
    return render(request, 'students/edit_student.html', {'form': form})
