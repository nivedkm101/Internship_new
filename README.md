# College Website (Django-based)

## Overview
This project is a Django-based web application that serves as the official website for a college. It provides information about faculty, research, academic programs, alumni, and various other sections. The project is a migration from an AngularJS-based website to Django while maintaining the original structure and design.

  
## Technologies Used
- **Frontend:** HTML, CSS, JavaScript (Migrated from AngularJS)
- **Backend:** Django (Python)
<!-- - **Database:** MySQL / PostgreSQL (as per requirements) -->
- **Templates:** Django Template Engine
<!-- - **Authentication:** Django Authentication System (for role-based access control) -->

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Django (>= 4.0)
- MySQL/PostgreSQL
- Virtual Environment (optional but recommended)

### Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/college-website.git
   cd college-website
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',  # Change to 'postgresql' if using PostgreSQL
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '3306',  # Change to '5432' for PostgreSQL
       }
   }
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Access the website at:
   ```
   http://127.0.0.1:8000/
   ```

## File Structure
```
college-website/
│── core/                   # Main app for handling general pages
│── academics/              # App for managing academic programs
│── alumni/                 # App for alumni-related content
│── faculty/                # App for faculty & staff directory
│── research/               # App for research & consultancy content
│── static/                 # Static files (CSS, JS, images)
│── templates/              # HTML templates
│── db.sqlite3              # Database (if using SQLite for testing)
│── manage.py               # Django project manager
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## Contact
For any queries, reach out to **Nived K M** at **nivedkm101@gmail.com**.

