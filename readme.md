# Student Management System

## Project Overview
The **Student Management System** is a Django web application that allows users to manage student records. It provides features for adding, editing, viewing, and deleting student information. Additional functionalities include user authentication, search, pagination, and custom error handling.

## Features
- **Student CRUD Operations:** Create, read, update, and delete student records.
- **Search Functionality:** Search students by first name or last name.
- **Pagination:** Paginate the student list view to display a limited number of records per page.
- **User Authentication:** Restrict access to create, edit, and delete operations to authenticated users.
- **Custom Error Handling:** Display custom 404 and 500 error pages.

## Technologies Used
- Python 3.x
- Django 4.x
- HTML, CSS, Bootstrap (for frontend styling)

## Setup Instructions

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.8 or higher
- Django 4.0 or higher
- Git (for version control)

### Step 1: Clone the Repository
Clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/upadhyaymohit28/student_management.git

###Step 2: Create and Activate a Virtual Environment

python -m venv env
source env/bin/activate  # For Mac/Linux
.\env\Scripts\activate  # For Windows

###Step 3: Install Project Dependencies
Step 3: Install Project Dependencies
bash
Copy code
pip install -r requirements.txt


###Step 4: Apply Database Migrations
bash
Copy code
python manage.py migrate


###Step 5: Create a Superuser
bash
Copy code
python manage.py createsuperuser


###Step 6: Run the Server
bash
Copy code
python manage.py runserver



###Step 7: Access the Application
Application: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/


###Project Structure
Copy code
student_management/
├── students/
├── student_management/
├── manage.py
├── README.md
└── requirements.txt


###Challenges Encountered
Handling date formats in form fields.
Implementing pagination and search functionality.
Setting up authentication and authorization.


###How to Contribute
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.