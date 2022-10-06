from email.policy import default
from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    # Permite ver el atributo "name" en la tabla de projectos del panel de administracion

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name
