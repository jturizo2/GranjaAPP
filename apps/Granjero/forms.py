from django import forms
from apps.Granjero.models import propietario

class propietario_form(forms.ModelForm):
    class Meta:
        model = propietario

        fields = [
                'name', 
                'LastName', 
                'correo',
                'Telefono',
                'imagePropietario',
                'imageHierro',
        ]
        labels = {
                'name': 'Nombre',
                'LastName': 'Apellido',
                'correo': 'Correo electrónico',
                'Telefono': 'Telefono',
                'imagePropietario': 'Propietario',
                'imageHierro': 'Hierro',
        }
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'LastName': forms.TextInput(attrs={'class': 'form-control'}),
                'correo': forms.TextInput(attrs={'class': 'form-control'}),
                'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }