from django import forms
from apps.trans.models import serviInsu,transaction

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

class mov_form(forms.ModelForm):
    class Meta:
        model = transaction
        fields = [
                'classTrans',
                'date',
                'AnimalCode',
                'detail',
                'Value',
        ]

        labels = {
                'classTrans':'Tipo de movimiento',
                'date':'Fecha de nacimiento',
                'AnimalCode':'Código de animal',
                'detail':'Detalle del movimiento',
                'Value':'Costo',
        }
        widgets = {
                'classTrans':forms.Select(attrs={'class': 'form-control'}),
                'date':forms.DateInput(attrs={'class': 'form-control'}),
                'AnimalCode':forms.Select(attrs={'class': 'form-control'}),
                'detail':forms.TextInput(attrs={'class': 'form-control'}),
                'Value':forms.NumberInput(attrs={'class': 'form-control'}),
        }   

class movFilter(forms.ModelForm):
    class Meta:
        model = transaction
        fields = [
                'classTrans',
                'date',
                'AnimalCode',
        ]

        labels = {
                'classTrans': 'Tipo de comercio',
                'date': 'Fecha de transacción',
                'AnimalCode': 'Código de animal',
        }
        widgets = {
                'classTrans': forms.Select(attrs={'class': 'form-control'}),
                'date': forms.DateInput(attrs={'class': 'form-control'}),
                'AnimalCode': forms.TextInput(attrs={'class': 'form-control'}),
        }