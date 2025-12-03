Project Planner WebApp
A robust Django-based web application designed to help users manage projects and create detailed plans with rich text content. The application features a modern Dark UI, secure user authentication, and a structured database backend using PostgreSQL.

🌟 Features
User Authentication System: Secure Registration, Login, and Logout functionality using Django's built-in auth system extended with a custom User model.

Project Management: Users can create, view, and organize multiple projects. Each project tracks a name, description, and modification timestamps.

Detailed Planning: Inside each project, users can create specific "Plans".

Rich Text Editing: Integrated CKEditor allows users to write detailed plans with formatting, lists, and image uploads.

Modern Dark UI: A custom-styled interface using Bootstrap 5 and custom CSS variables for a consistent dark theme with orange/teal accents.

Responsive Design: Sidebar navigation and responsive layouts for mobile and desktop usage.

Dynamic Sidebar: Automatically lists the user's active projects for quick navigation.

🛠️ Tech Stack
Backend: Python 3.12, Django 5.x

Database: PostgreSQL

Containerization: Docker & Docker Compose

Frontend: HTML5, Bootstrap 5, Custom CSS

Utilities:

django-ckeditor & django-ckeditor-uploader (Rich Text)

django-widget-tweaks (Form rendering)

🚀 Getting Started
Prerequisites
Docker and Docker Compose installed on your machine.

(Optional) Python 3.10+ if running locally without Docker.

🐳 Run with Docker (Recommended)
This project is configured to run seamlessly with Docker.

Clone the repository:

Bash

git clone https://github.com/yourusername/project-planner.git
cd project-planner
Build and Start the containers:

Bash

docker-compose up --build
This will start the Django web server on port 8000 and the PostgreSQL database on port 5432.

Apply Migrations: Open a new terminal window and run:

Bash

docker-compose exec web python manage.py migrate
Create a Superuser (Admin):

Bash

docker-compose exec web python manage.py createsuperuser
Access the App:

Web App: http://localhost:8000

Admin Panel: http://localhost:8000/admin

🔧 Manual Local Installation
If you prefer not to use Docker:

Create a virtual environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Configure Database: Ensure you have a PostgreSQL database running. Update DATABASES in Project_Manager_WebApp/settings.py with your credentials.

Run Migrations:

Bash

python manage.py migrate
Run Server:

Bash

python manage.py runserver
📂 Project Structure
accounts/: Handles user registration, custom User model, and authentication logic.

project_manager/: Core app containing logic for Projects and Plans models, views, and forms.

templates/: Contains HTML templates (Base, Home, Login, Register, Project details).

static/: CSS styles, images, and JavaScript files.

uploads/: Directory for media files uploaded via CKEditor.

📸 Screenshots
(You can add screenshots of your application here, e.g., the Login screen, the Dashboard, and the Plan Editor).

🛡️ License
This project is free to use.
