# Project Management Application

A Django-based web application for project and task management.

## Features

- **Project Management**: Create, view, update, and delete projects.
- **Task Management**: Create, view, update, and delete tasks within each project. Includes task dependencies.
- **Team Collaboration**: Assign tasks to team members and receive notifications for task assignments and due dates.
- **User Interface**: Intuitive UI for accessing project and task management functionalities.
- **Authentication and Authorization**: Secure access to the application with user authentication.
- **Gantt Chart**: Visualize project timelines and task dependencies.
- **Workload Tracking**: Track team members' workloads and allocate tasks based on availability.

## Setup Instructions

### Prerequisites

- Python 3.12+
- Django 5.0
- Git

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AunRaza21/project_management.git
    cd project_management
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup database**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

- **Admin Interface**: Access the Django admin interface at `http://127.0.0.1:8000/admin` to manage users, projects, and tasks.
- **Project Management**: Create, update, and delete projects.
  - URL: `/projects/`
- **Task Management**: Create, update, and delete tasks within projects. Assign tasks to team members and set dependencies.
  - URL: `/projects/<project_id>/tasks/`
- **Gantt Chart**: Visualize project timelines and task dependencies.
  - URL: `/projects/<project_id>/gantt/`
- **Workload Tracking**: Track team members' workloads.
  - URL: `/projects/<project_id>/track_workloads/`
- **Real-time Collaboration**: Access the chat interface for project discussions and task updates.
  - URL: `/projects/<project_id>/chat/`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Django and the open-source community for their contributions.

