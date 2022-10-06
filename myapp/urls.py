from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("tasks/", views.tasks),
    path("create_task/", views.create_task),
    path("projects/", views.projects),
    # Permite recibir parametros especificos por la url
    path("aloha/<str:username>", views.aloha),
]
