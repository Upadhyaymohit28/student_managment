
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # First name of the student
    last_name = models.CharField(max_length=100)  # Last name of the student
    email = models.EmailField()  # Email field for student email
    date_of_birth = models.DateField()  # Date of birth of the student
    enrollment_date = models.DateField()  # Enrollment date of the student
    grade = models.IntegerField()  # Grade level of the student

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
