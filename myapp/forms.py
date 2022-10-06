from cProfile import label
from django import forms
from pkg_resources import require


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)
    description = forms.CharField(label='Descripcion', widget=forms.Textarea)
