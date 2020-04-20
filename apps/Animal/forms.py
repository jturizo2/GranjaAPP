from django import forms
from apps.Animal.model import animal

class animalForm(forms.ModelForm):
    class Meta:
        model = animal

        fields = [
                'Codigo_animal',
                'IdGranja',
                'concepto',
                'nombre',
                'Valor_inicial',
                'Genero',
                'Etapa_productiva',
                'Raza',
                'Hierro',
                'Proposito',
                'Fecha_recibida',
                'Fecha_nacimiento',
                'Código_mama',
                'Código_papa',
        ]

        labels = {
                'Codigo_animal': 'Código de animal'
                'IdGranja': 'Granja'
                'concepto': 'Concepto de adquisición'
                'nombre': 'Nombre del animal'
                'Valor_inicial': 'Valor inicial [$]'
                'Genero': 'Genero'
                'Etapa_productiva': 'Etapa Productiva'
                'Raza': 'Raza'
                'Hierro': 'Hierro'
                'Proposito': 'Propósito'
                'Fecha_recibida': 'Fecha recibido'
                'Fecha_nacimiento': 'Fecha nacimiento'
                'Código_mama': 'Código madre'
                'Código_papa': 'Código padre' 
        }

        widgets = {
                'Codigo_animal': forms.TextInput(attrs={'class': 'form-control'}),
                'IdGranja': forms.Select(attrs={'class': 'form-control'}),
                'concepto': forms.Select(attrs={'class': 'form-control'}),
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'Valor_inicial': forms.TextInput(attrs={'class': 'form-control'}),
                'Genero': forms.Select(attrs={'class': 'form-control'}),
                'Etapa_productiva': forms.Select(attrs={'class': 'form-control'}),
                'Raza': forms.Select(attrs={'class': 'form-control'}),
                'Hierro': forms.Select(attrs={'class': 'form-control'}),
                'Proposito': forms.Select(attrs={'class': 'form-control'}),
                'Fecha_recibida': forms.SelectDateWidget(attrs={'class': 'form-control'}),
                'Fecha_nacimiento': forms.SelectDateWidget(attrs={'class': 'form-control'}),
                'Código_mama': forms.TextInput(attrs={'class': 'form-control'}),
                'Código_papa': forms.TextInput(attrs={'class': 'form-control'}),
        }