from django import forms
from apps.Granja.models import granja

class granja_from(forms.ModelForm):
    class Meta:
        model = granja
        fields = [
                'Cod',
                'Name',
                'Details',
                'Hec',
                'Div',
                'NumPozos',
                'image',
        ]

        labels = {
                'Cod': 'Codigo de granja',
                'Name':'Nombre',
                'Details': 'Detalle',
                'Hec': 'Número de hectareas',
                'Div': 'Número de diviciones',
                'NumPozos': 'Numero de pozos',
                'image': 'Imagen'
        }

        widgets = {
                'Cod': forms.TextInput(attrs={'class': 'form-control'}),
                'Name': forms.TextInput(attrs={'class': 'form-control'}),
                'Details': forms.TextInput(attrs={'class': 'form-control'}),
                'Hec': forms.NumberInput(attrs={'class': 'form-control'}),
                'Div':forms.NumberInput(attrs={'class': 'form-control'}),
                'NumPozos': forms.NumberInput(attrs={'class': 'form-control'}),
        }