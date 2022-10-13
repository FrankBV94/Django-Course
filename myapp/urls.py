from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("tasks/", views.tasks, name="tasks"),
    path("projects/", views.projects, name="projects"),
    path("create_task/", views.create_task, name="create_task"),
    path("create_project/", views.create_project, name="create_project"),
    path("project_detail/<int:id>", views.project_detail, name="project_detail"),
    # Permite recibir parametros especificos por la url
    path("aloha/<str:username>", views.aloha, name="aloha"),
]
