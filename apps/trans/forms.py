from django import forms
from apps.trans.models import serviInsu

class serviInsu_form(forms.ModelForm):
    class Meta:
        model = serviInsu
        fields = [
                'Tipo',
                'Nombre',
                'Valor_Unidad',
                'Detalle',
                'Proveedor',
                'Telefono',
        ]

        labels = {
                'Tipo': 'Insumo o Servicio',
                'Nombre': 'Nombre',
                'Valor_Unidad': 'Valor Unitario',
                'Detalle': 'Detalle',
                'Proveedor': 'Proveedor',
                'Telefono': 'Telefono',
        }
        widgets = {
                'Tipo': forms.Select(attrs={'class': 'form-control'}),
                'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'Valor_Unidad': forms.NumberInput(attrs={'class': 'form-control'}),
                'Detalle': forms.TextInput(attrs={'class': 'form-control'}),
                'Proveedor': forms.TextInput(attrs={'class': 'form-control'}),
                'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        