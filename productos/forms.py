from django import forms
from .models import Categoria 

from django.forms import ModelForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria",]
        labels ={'categoria': 'Categoría',}
