# Project Planner WebApp

**Project Planner WebApp** is a robust Django-based web application designed to help users manage projects and create detailed plans with rich text content. The application features a modern Dark UI, secure user authentication, and a structured database backend using PostgreSQL.

## 🌟 Features

* **User Authentication System:**
    * Secure Registration, Login, and Logout functionality.
    * Custom User model integration.
* **Project Management:**
    * Create, view, and organize multiple projects.
    * Each project tracks a name, description, and modification timestamps.
    * Dashboard view listing all user projects.
* **Detailed Planning:**
    * Create specific "Plans" within each project.
    * **Rich Text Editing:** Integrated **CKEditor** allows users to write detailed plans with formatting, lists, and image uploads.
* **Modern UI/UX:**
    * Custom-styled interface using **Bootstrap 5**.
    * **Dark Mode** theme with vibrant orange and teal accents.
    * Responsive design suitable for both mobile and desktop.
    * Dynamic sidebar for quick navigation.

## 🛠️ Tech Stack

* **Backend:** Python 3.12, Django 5.x
* **Database:** PostgreSQL
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Utilities:**
    * `django-ckeditor` & `django-ckeditor-uploader` (Rich Text)
    * `django-widget-tweaks` (Form rendering)
* **DevOps:** Docker & Docker Compose

## 🚀 Getting Started

The project is configured to run seamlessly using **Docker**.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed.
* Git.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPO_URL>
    cd project-planner-webapp
    ```

2.  **Build and Start the containers:**
    Run the following command to build the images and start the services (Web & DB):
    ```bash
    docker-compose up --build
    ```
    *This starts the web server on port `8000` and the PostgreSQL database on port `5432`.*

3.  **Apply Database Migrations:**
    Open a new terminal window and run:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4.  **Create a Superuser (Optional):**
    To access the Django Admin panel:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5.  **Access the Application:**
    Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)

## 📂 Project Structure

* `accounts/`: Handles user authentication (login, register, custom User model).
* `project_manager/`: Core application containing logic for Projects and Plans (models, views, forms).
* `templates/`: HTML templates (Base, Home, Project details, etc.).
* `static/`: CSS styles (including custom dark theme) and static assets.
* `media/`: Directory for user-uploaded content (via CKEditor).
* `docker-compose.yml`: Docker services configuration.

## ⚙️ Environment Configuration

The project is set up for local development with the following default settings (found in `settings.py` and `docker-compose.yml`):

* **Debug:** `True`
* **Database Name:** `project_manager_db`
* **Database User:** `user`
* **Database Password:** `password`

---

**Developed by:** Veselin15
