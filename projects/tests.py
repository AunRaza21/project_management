# tests.py
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Project, Task
from datetime import date

class ProjectManagementTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')

        # Create a project
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            start_date=date.today(),
            end_date=date.today()
        )
        self.project.team_members.add(self.user)
        
        # Create a task
        self.task = Task.objects.create(
            project=self.project,
            title='Test Task',
            description='Test Task Description',
            priority='Medium',
            due_date=date.today(),
            status='In Progress'
        )

    def test_create_project(self):
        response = self.client.post(reverse('project_create'), {
            'title': 'New Project',
            'description': 'New Description',
            'start_date': date.today(),
            'end_date': date.today(),
            'team_members': [self.user.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project.objects.count(), 2)

    def test_update_project(self):
        response = self.client.post(reverse('project_update', args=[self.project.pk]), {
            'title': 'Updated Project',
            'description': 'Updated Description',
            'start_date': self.project.start_date,
            'end_date': self.project.end_date,
            'team_members': [self.user.id]
        })
        self.assertEqual(response.status_code, 302)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Updated Project')

    def test_delete_project(self):
        response = self.client.post(reverse('project_delete', args=[self.project.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Project.objects.count(), 0)

    def test_create_task(self):
        response = self.client.post(reverse('task_create', args=[self.project.pk]), {
            'title': 'New Task',
            'description': 'New Task Description',
            'priority': 'High',
            'due_date': date.today(),
            'status': 'In Progress',
            'dependencies': [],
            'assigned_to': self.user.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)

    def test_update_task(self):
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': 'Task Updated',
            'description': 'Updated Task Description',
            'priority': 'Low',
            'due_date': self.task.due_date,
            'status': 'Completed',
            'dependencies': [],
            'assigned_to': self.user.id
        })
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Task Updated')
        self.assertEqual(self.task.status, 'Completed')

    def test_delete_task(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_assignment(self):
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': self.task.title,
            'description': self.task.description,
            'priority': self.task.priority,
            'due_date': self.task.due_date,
            'status': self.task.status,
            'dependencies': [],
            'assigned_to': self.user.id
        })
        self.assertEqual(response.status_code, 200)

    def test_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/projects/')

    def test_generate_gantt_chart(self):
        response = self.client.get(reverse('generate_gantt_chart', args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)

    def test_real_time_collaboration(self):
        response = self.client.get(reverse('real_time_collaboration', args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)
