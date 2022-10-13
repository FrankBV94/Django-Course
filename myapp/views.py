from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewProject, CreateNewTask

# Create your views here.


def index(request):
    title = "Aloha!!"
    return render(
        request,
        "index.html",
        {
            "title": title,
        },
    )


def aloha(request, username):
    print(username)
    return HttpResponse("<h1>Aloha %s<h1>" % username)


def about(request):
    username = "Frank"
    return render(request, "about.html", {"username": username})


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(request, "create_project.html", {"form": CreateNewProject()})
    else:
        project = Project.objects.create(name=request.POST["name"])
        return redirect("projects")


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "project_detail.html", {"project": project, "tasks": tasks})
