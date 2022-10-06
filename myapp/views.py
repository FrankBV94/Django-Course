from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask
# Create your views here.


def index(request):
    title = 'Aloha!!'
    return render(request, 'index.html', {
        'title': title,
    })


def aloha(request, username):
    print(username)
    return HttpResponse("<h1>Aloha %s<h1>" % username)


def about(request):
    username = 'Frank'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    Task.objects.create(title=request.GET['title'], description=request.GET['description'], project=1)
    return render(request, 'create_task.html', {
        'form': CreateNewTask()
    })
