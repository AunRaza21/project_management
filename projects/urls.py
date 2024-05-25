from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:pk>/task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('project/<int:pk>/gantt/', views.generate_gantt_chart, name='generate_gantt_chart'),
    path('project/<int:pk>/workloads/', views.track_workloads, name='track_workloads'),
    path('project/<int:pk>/collaboration/', views.real_time_collaboration, name='real_time_collaboration'),
    path('project/<int:project_id>/chat/', views.chat, name='chat'),

]
