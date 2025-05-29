# College Website (Django-based)

## About the Project
This project is a Django-based web application developed as part of an internship program. It serves as the official website for a college, providing information about faculty, research, academic programs, alumni, and other institutional details. The project is a migration from an AngularJS-based website to Django while maintaining the original structure and design.

The website is designed to be dynamic, responsive, and user-friendly, allowing administrators to manage content efficiently while providing students and visitors with easy access to information.

### Key Features
- **Dynamic Content Management:** Easily update and manage website content.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Role-Based Access Control:** Secure login system for administrators and staff.
- **Multilingual Support:** Includes translations for various languages.
- **Database Integration:** Efficient data storage and retrieval using a relational database.
- **Scalable Architecture:** Designed to accommodate future enhancements.

---
## Few Snapshots 
![Screenshot 2025-05-14 020140](https://github.com/user-attachments/assets/6fa2e2ec-2f02-46e5-a1fa-13b36aa3d96a)
![Screenshot 2025-05-14 020304](https://github.com/user-attachments/assets/2f478277-fa94-4cda-a43d-44cd66c85ce6)
![Screenshot 2025-05-14 020746](https://github.com/user-attachments/assets/78b5c7af-630e-4a45-ad00-faaa5f0d9430)
![Screenshot 2025-05-14 020948](https://github.com/user-attachments/assets/ab2f0784-989b-4b80-8f89-93544bc9670d)
![Screenshot 2025-05-14 021520](https://github.com/user-attachments/assets/25db047e-617f-40bf-aa39-639203f25728)
![Screenshot 2025-05-14 021906](https://github.com/user-attachments/assets/a8b481c8-aa3e-467a-8aff-ad7f6be14442)
![Screenshot 2025-05-14 020049](https://github.com/user-attachments/assets/5dd4f8ed-13aa-4c8e-a956-552346f00027)


---

## Project Structure
The project follows a modular structure for better maintainability and scalability. Below is the folder structure:


W:\PTU WORKS\Internship\NIT Py\Internship_new\website
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database file (if used)
├── my_django_project/        # Main Django project folder
│   ├── __init__.py           # Marks the directory as a Python package
│   ├── asgi.py               # ASGI configuration for asynchronous support
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing for the project
│   ├── wsgi.py               # WSGI configuration for deployment
├── apps/                     # Folder for Django apps
│   ├── core/                 # Core app for common functionality
│   │   ├── __init__.py       # Marks the directory as a Python package
│   │   ├── admin.py          # Admin interface configuration
│   │   ├── apps.py           # App configuration
│   │   ├── models.py         # Database models
│   │   ├── tests.py          # Unit tests
│   │   ├── views.py          # Views for handling requests
│   │   └── migrations/       # Database migrations
│   │       ├── __init__.py   # Marks the directory as a Python package
│   └── other_apps/           # Additional apps (e.g., announcements, institute)
├── templates/                # HTML templates for the project
│   ├── base.html             # Base template for the website
│   └── other_templates/      # Additional templates for specific pages
├── static/                   # Static files (CSS, JavaScript, images)
│   ├── css/                  # CSS files
│   ├── js/                   # JavaScript files
│   └── images/               # Image files
└── requirements.txt          # Python dependencies



---

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript (Migrated from AngularJS)
- **Backend:** Django (Python)
- **Templates:** Django Template Engine
- **Database:** MySQL/PostgreSQL (configurable)
- **Environment:** Virtual Environment for dependency management

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Django (>= 4.0)
- MySQL/PostgreSQL
- Git (for version control)
- Virtual Environment (optional but recommended)

### Steps to Run the Project
1. **Clone the Repository:**
   Navigate to the desired directory and clone the project repository:
   ```bash
   git clone <repository-url>

   cd Internship_new
   cd website\my_django_project


2. **Run the Development Server: Start the Django development server:
    python manage.py runserver
