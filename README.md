# 🎓 Course Management System Using Python OOPs

A Python-based Course Management System demonstrating **Object-Oriented Programming (OOP)** concepts, modular programming, exception handling, logging, unit testing, and Git/GitHub version control.

This project is developed as a final mini-project to demonstrate how Python OOP concepts can be integrated into a real-world application and managed using a professional Git workflow.

## 📌 Project Overview

The Course Management System is a console-based Python application designed to manage students, mentors, courses, and enrollments.

The system allows users to:

- Create students and mentors.
- Create courses and assign mentors.
- Enroll students in courses.
- Validate course capacity.
- Prevent duplicate enrollments.
- Track assignment submissions.
- Display student, mentor, course, and enrollment information.
- Handle errors through custom exceptions.
- Record application activities using logging.
- Execute automated unit tests.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Application development |
| Python OOP | Object-oriented design |
| ABC Module | Abstraction |
| Logging Module | Application activity tracking |
| Unittest | Automated testing |
| Git | Version control |
| GitHub | Repository hosting and collaboration |
| VS Code | Development environment |

## 🏗️ Project Architecture

```text
                 User (Abstract Class)
                         |
               +---------+---------+
               |                   |
            Student              Mentor
               |                   |
               |                   |
               +------ Course -----+
                          |
                      Enrollment
                          |
                    Student + Course
```

**Class Responsibilities**

| Class | Responsibility |
|---|---|
| User | Abstract base class containing common user attributes |
| Student | Manages student information, enrolled courses, and assignments |
| Mentor | Manages mentor information and assigned courses |
| Course | Manages course details, capacity, and mentor assignment |
| Enrollment | Connects students with courses and manages enrollment status |

## 📂 Project Structure

```text
course-management-system/
│
├── course_management/
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── mentor.py
│   ├── course.py
│   ├── enrollment.py
│   ├── exceptions.py
│   └── logger_config.py
│
├── tests/
│   └── test_course_management.py
│
├── logs/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🧠 OOP Concepts Demonstrated

### 1. Abstraction

The `User` class uses Python's `ABC` and `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def display_info(self):
        pass
```

This ensures that concrete subclasses implement `display_info()`.

### 2. Inheritance

The `Student` and `Mentor` classes inherit common attributes and methods from `User`.

```python
class Student(User):
    pass

class Mentor(User):
    pass
```

### 3. Encapsulation

Internal attributes are protected through controlled access.

```python
self._email = email
self.__capacity = capacity
```

Properties allow controlled access to selected attributes.

### 4. Polymorphism

Both `Student` and `Mentor` implement `display_info()` differently.

```python
users = [student1, mentor1]

for user in users:
    print(user.display_info())
```

The same method call produces role-specific information.

### 5. Instance Methods

Instance methods operate on individual objects.

Examples include:

- `student.submit_assignment()`
- `course.assign_mentor(mentor)`
- `enrollment.enroll()`
- `course.display_course()`

### 6. Static Methods

Static methods perform operations without requiring instance or class state.

```python
Course.validate_capacity(10)
User.validate_email("student@example.com")
```

### 7. Class Methods

Class methods access class-level information.

```python
User.get_total_users()
Course.get_total_courses()
Enrollment.get_total_enrollments()
```

## ⚙️ Installation and Setup

**Prerequisites**

- Python 3.10 or above
- Git
- VS Code or another Python-compatible IDE

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/course-management-system.git
```

Replace `YOUR-USERNAME` with your actual GitHub username and adjust the repository name if necessary.

**Step 2: Navigate to the project**

```bash
cd course-management-system
```

**Step 3: Create a virtual environment (optional)**

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**Step 4: Install dependencies**

```bash
python -m pip install -r requirements.txt
```

The project currently uses Python standard-library modules and does not require external packages.

**Step 5: Run the application**

```bash
python main.py
```

## 💻 Example Execution

The following is an illustrative example of the application's output.

```text
============================================================
COURSE MANAGEMENT SYSTEM
============================================================

Student Created:
Student ID: S101
Name: Ananya
Email: ananya@gmail.com

Mentor Created:
Mentor ID: M101
Name: Raj
Expertise: Python

Course Created:
Course ID: C101
Course: Python OOP Masterclass
Duration: 8 Weeks
Capacity: 2

Enrollment Successful:
Enrollment ID: E101
Student: Ananya
Course: Python OOP Masterclass
Status: Active

============================================================
SYSTEM STATISTICS
============================================================

Total Users: 5
Total Courses: 2
Total Enrollments: 2
```

## 🛡️ Exception Handling

The application implements custom exceptions to handle invalid operations.

| Exception | Description |
|---|---|
| `CourseManagementError` | Base application exception |
| `InvalidEmailError` | Invalid email address |
| `InvalidCapacityError` | Invalid course capacity |
| `CourseFullError` | Course has no available seats |
| `DuplicateEnrollmentError` | Student is already enrolled |
| `InvalidEnrollmentError` | Invalid enrollment information |

Example:

```python
try:
    enrollment.enroll()
except DuplicateEnrollmentError as error:
    print("Enrollment failed:", error)
```

## 📝 Application Logging

The application uses Python's built-in `logging` module.

Logs are written to:

```text
logs/application.log
```

Example log messages:

```text
INFO - Student created: Ananya
INFO - Course created: Python OOP Masterclass
INFO - Enrollment successful
WARNING - Duplicate enrollment attempt
```

Log files are excluded from Git version control through `.gitignore`.

## 🧪 Unit Testing

The project uses Python's built-in `unittest` framework.

Run all tests:

```bash
python -m unittest discover -s tests -v
```

Tests cover:

- Student creation
- Mentor creation
- Course creation
- Invalid email validation
- Invalid course capacity
- Successful enrollment
- Duplicate enrollment prevention
- Course capacity limits

## 🌿 Git and GitHub Workflow

The project demonstrates version control through feature branches, meaningful commits, and Pull Requests.

**Example Branch Structure**

```text
main
 |
 +---- feature/user-management
 |
 +---- feature/course-management
 |
 +---- feature/enrollment
 |
 +---- feature/course-search
```

Only branches actually created and pushed during development will appear in GitHub.

**Common Git Commands**

| Command | Purpose |
|---|---|
| `git init` | Initialize a repository |
| `git status` | Check working directory status |
| `git branch` | View local branches |
| `git switch -c feature/name` | Create and switch to a feature branch |
| `git add .` | Stage changes |
| `git commit -m "message"` | Save a commit |
| `git push` | Upload commits to GitHub |
| `git fetch` | Download remote updates without merging |
| `git pull` | Fetch and integrate remote changes |
| `git merge` | Merge branches |
| `git log --oneline --graph --all` | View commit history |

**Pull Request Workflow**

```text
Create Feature Branch
         |
         v
Implement Feature
         |
         v
Run Unit Tests
         |
         v
Commit Changes
         |
         v
Push Branch to GitHub
         |
         v
Create Pull Request
         |
         v
Review Changes
         |
         v
Merge into Main
         |
         v
Pull Updated Main Locally
```

## 🚀 Future Enhancements

- Database integration using SQLite or PostgreSQL
- Student and mentor authentication
- REST APIs using FastAPI
- Course search and filtering
- Student progress dashboards
- Course completion certificates
- Web-based user interface
- Continuous integration using GitHub Actions

## 🎥 YouTube Project Walkthrough

A project walkthrough demonstrates:

1. Problem statement and requirements
2. System architecture and class relationships
3. Python OOP concepts
4. Package and module structure
5. Important code implementations
6. Application execution
7. Exception handling and logging
8. Unit testing
9. Git branching and commit history
10. GitHub Pull Request and merge workflow

**YouTube Video:** Add your published video URL here.

## 👩‍💻 Author

**Amrutha Varshini Alva**

YouTube Channel: **Evolve with Amrutha Varshini Alva**

*Keep learning, keep building, and keep evolving.*

## 📄 License

No license has been specified for this project.
