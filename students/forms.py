from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']
    
    # Validation for email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Only example.com emails are allowed.")
        return email

    # Validation for grade field
    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if not (1 <= grade <= 12):
            raise forms.ValidationError("Grade must be between 1 and 12.")
        return grade
