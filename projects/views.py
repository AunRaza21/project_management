from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.shortcuts import render, get_object_or_404
from datetime import date
import json

@login_required
def project_list(request):
    projects = Project.objects.filter(team_members=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            project.team_members.add(request.user)
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

@login_required
def task_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'project': task.project})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('project_detail', pk=task.project.pk)
    return render(request, 'projects/task_confirm_delete.html', {'task': task, 'project': task.project})

@login_required
def real_time_collaboration(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Implement real-time collaboration logic here
    return render(request, 'projects/chat.html', {'project': project})

@login_required
def track_workloads(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    
    # Example logic to track workloads
    workload = {}
    for task in tasks:
        assigned_to = task.assigned_to
        if assigned_to:
            if assigned_to not in workload:
                workload[assigned_to] = 0
            workload[assigned_to] += 1  # or any other logic to calculate workload

    context = {
        'project': project,
        'workload': workload,
    }
    return render(request, 'projects/workload.html', context)

def chat(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/chat.html', {'project': project})

@login_required
def generate_gantt_chart(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)

    task_data = []
    for task in tasks:
        task_data.append([
            str(task.id),  # Task ID
            task.title,  # Task Name
            '',  # Resource
            date.today().isoformat(),  # Start Date
            task.due_date.isoformat(),  # End Date
            None,  # Duration (not needed when start and end are defined)
            0,  # Percent complete
            None  # Dependencies
        ])

    context = {
        'project': project,
        'task_data': json.dumps(task_data),  # Serialize the data to JSON
    }
    print(task_data)  # Debug print to check data
    return render(request, 'projects/gantt.html', context)
