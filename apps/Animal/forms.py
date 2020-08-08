from django import forms
from apps.Animal.models import animal, concepto, genero, etapa_productiva, raza,proposito

class animalForm(forms.ModelForm):
    class Meta:
        model = animal
        fields = [
                'estado',
                'Codigo_animal',
                'concepto',
                'nombre',
                'Valor_inicial',
                'Genero',
                'Etapa_productiva',
                'Raza',
                'propietario',
                'Proposito',
                'Fecha_recibida',
                'Fecha_nacimiento',
                'Código_mama',
                'Código_papa',
                'image',
        ]

        labels = {
                'estado':'Estado',
                'Codigo_animal': 'Código de animal',
                'concepto': 'Concepto de adquisición',
                'nombre': 'Nombre del animal',
                'Valor_inicial': 'Valor inicial [$]',
                'Genero': 'Genero',
                'Etapa_productiva': 'Etapa Productiva',
                'Raza': 'Raza',
                'Propietario': 'Propietario',
                'Proposito': 'Propósito',
                'Fecha_recibida': 'Fecha recibido',
                'Fecha_nacimiento': 'Fecha nacimiento',
                'Código_mama': 'Código madre',
                'Código_papa': 'Código padre',
                'image': 'Imagen',
        }
        widgets = {
                'estado': forms.TextInput(attrs={'class': 'form-control'}),
                'Codigo_animal': forms.TextInput(attrs={'class': 'form-control'}),
                'concepto': forms.Select(attrs={'class': 'form-control'}),
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'Valor_inicial': forms.TextInput(attrs={'class': 'form-control'}),
                'Genero': forms.Select(attrs={'class': 'form-control'}),
                'Etapa_productiva': forms.Select(attrs={'class': 'form-control'}),
                'Raza': forms.Select(attrs={'class': 'form-control'}),
                'propietario': forms.Select(attrs={'class': 'form-control'}),
                'Proposito': forms.Select(attrs={'class': 'form-control'}),
                'Fecha_recibida': forms.DateInput(attrs={'class': 'form-control'}),
                'Fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
                'Código_mama': forms.TextInput(attrs={'class': 'form-control'}),
                'Código_papa': forms.TextInput(attrs={'class': 'form-control'}),
        }
class concepto_form(forms.ModelForm):
    class Meta:
        model = concepto
        fields = [
                'concepto',
                'detalle_concepto',
        ]

        labels = {
                'concepto': 'Concepto',
                'detalle_concepto': 'Detalle de comcepto',
        }
        widgets = {
                'concepto': forms.TextInput(attrs={'class': 'form-control'}),
                'detalle_concepto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class genero_form(forms.ModelForm):
    class Meta:
        model = genero
        fields = [
                'genero',
        ]

        labels = {
                'genero': 'Genero',
        }
        widgets = {
                'genero': forms.TextInput(attrs={'class': 'form-control'}),
        }
class eProductiva_form(forms.ModelForm):
    class Meta:
        model = etapa_productiva
        fields = [
                'etapa_prod',
        ]

        labels = {
                'etapa_prod': 'Etapa productiva',
        }
        widgets = {
                'etapa_prod': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class raza_form(forms.ModelForm):
    class Meta:
        model = raza
        fields = [
                'raza',
        ]

        labels = {
                'raza': 'Raza',
        }
        widgets = {
                'raza': forms.TextInput(attrs={'class': 'form-control'}),
        }

class proposito_form(forms.ModelForm):
    class Meta:
        model = proposito
        fields = [
                'tipo_proposito',
        ]

        labels = {
                'tipo_proposito': 'Tipo de proposito',
        }
        widgets = {
                'tipo_proposito': forms.TextInput(attrs={'class': 'form-control'}),
        }
class animalFilter(forms.ModelForm):
    class Meta:
        model = animal
        fields = [
                'Codigo_animal',
                'concepto',
                'nombre',
                'Genero',
                'Etapa_productiva',
                'Raza',
                'propietario',
                'Proposito',
                'Fecha_recibida',
                'Fecha_nacimiento',
                'Código_mama',
                'Código_papa',
        ]

        labels = {
                'Codigo_animal': 'Código de animal',
                'concepto': 'Concepto de adquisición',
                'nombre': 'Nombre del animal',
                'Genero': 'Genero',
                'Etapa_productiva': 'Etapa Productiva',
                'Raza': 'Raza',
                'Propietario': 'Propietario',
                'Proposito': 'Propósito',
                'Fecha_recibida': 'Fecha recibido',
                'Fecha_nacimiento': 'Fecha nacimiento',
                'Código_mama': 'Código madre',
                'Código_papa': 'Código padre',
        }
        widgets = {
                'Codigo_animal': forms.TextInput(attrs={'class': 'form-control'}),
                'concepto': forms.Select(attrs={'class': 'form-control'}),
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'Genero': forms.Select(attrs={'class': 'form-control'}),
                'Etapa_productiva': forms.Select(attrs={'class': 'form-control'}),
                'Raza': forms.Select(attrs={'class': 'form-control'}),
                'propietario': forms.Select(attrs={'class': 'form-control'}),
                'Proposito': forms.Select(attrs={'class': 'form-control'}),
                'Fecha_recibida': forms.DateInput(attrs={'class': 'form-control'}),
                'Fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
                'Código_mama': forms.TextInput(attrs={'class': 'form-control'}),
                'Código_papa': forms.TextInput(attrs={'class': 'form-control'}),
        }