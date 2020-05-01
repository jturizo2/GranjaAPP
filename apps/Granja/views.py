from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,UpdateView, DeleteView,CreateView
from apps.Animal.models import concepto, genero, etapa_productiva,raza,proposito

from apps.Granjero.models import propietario
from apps.Granjero.forms import propietario_form

from apps.trans.models import serviInsu
from apps.trans.forms import serviInsu_form

from apps.Animal.forms import concepto_form, genero_form, eProductiva_form, raza_form, proposito_form

from apps.Granja.models import granja
from apps.Granja.forms import granja_from

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def granja_admin(request,id_granja):
    granj = granja.objects.filter(id=id_granja)[0]
    request.session['granja'] = granj.Name
    request.session['idgranja'] = granj.id
    contexto = {'granja': request.session['granja'],
                'idgranja': request.session['idgranja'],
                'granj':granj}
    return render(request, 'Granja/index.html', contexto)

@login_required
def granja_new(request):
    if request.method == 'GET':
        form = granja_from()
        return render (request,'Granja/new_granja.html',{'form': form})
    elif request.method == 'POST':
        form = granja_from(request.POST, request.FILES)
        if form.is_valid():
            new_granja = granja(user=request.user,
                                image=form.cleaned_data["image"],
                                Hec=form.cleaned_data["Hec"],
                                Cod=form.cleaned_data["Cod"],
                                Name=form.cleaned_data["Name"],
                                Details=form.cleaned_data["Details"],
                                Div=form.cleaned_data["Div"],
                                NumPozos=form.cleaned_data["NumPozos"]
                                )
            new_granja.save()
    return HttpResponseRedirect('/granja/listar')

class granja_list(ListView):
    model = granja
    template_name = 'Granja/granja_list.html'
    def get_queryset(self):
        return granja.objects.filter(user=self.request.user)


class granja_delete(DeleteView):
    model = granja
    template_name = 'Granja/granja_delete.html'
    success_url = reverse_lazy('granja:list')

class granja_edit(UpdateView):
    model = granja
    form_class = granja_from
    template_name = 'Granja/new_granja.html'
    success_url = reverse_lazy('granja:list')
    
# COnfiguración de la Granja
@login_required
def granja_config(request):
    contexto = {'granja': request.session['granja'],
                'idgranja': request.session['idgranja']}
    return render(request, 'Granja/granja_config.html',contexto)

# CRUD Conceptos
class granja_concepto_new(CreateView):
    model = concepto
    form_class = concepto_form
    template_name = 'Granja/concepto/granja_concepto_new.html'
    success_url = reverse_lazy('granja:list_concepto')

class granja_concepto_list(ListView):
    model = concepto
    template_name = 'Granja/concepto/granja_concepto_list.html'

class granja_concepto_delete(DeleteView):
    model = concepto
    template_name = 'Granja/concepto/granja_concepto_delete.html'
    success_url = reverse_lazy('granja:list_concepto')

class granja_concepto_edit(UpdateView):
    model = concepto
    form_class = concepto_form
    template_name = 'Granja/concepto/granja_concepto_new.html'
    success_url = reverse_lazy('granja:list_concepto')

# CRUD Genero
class granja_genero_new(CreateView):
    model = genero
    form_class = genero_form
    template_name = 'Granja/genero/granja_genero_new.html'
    success_url = reverse_lazy('granja:list_genero')

class granja_genero_list(ListView):
    model = genero
    template_name = 'Granja/genero/granja_genero_list.html'

class granja_genero_delete(DeleteView):
    model = genero
    template_name = 'Granja/genero/granja_genero_delete.html'
    success_url = reverse_lazy('granja:list_genero')

class granja_genero_edit(UpdateView):
    model = genero
    form_class = genero_form
    template_name = 'Granja/genero/granja_genero_new.html'
    success_url = reverse_lazy('granja:list_genero')
# CRUD Etapa productiva
class granja_eProductiva_new(CreateView):
    model = etapa_productiva
    form_class = eProductiva_form
    template_name = 'Granja/eProductiva/granja_eProductiva_new.html'
    success_url = reverse_lazy('granja:list_eProductiva')

class granja_eProductiva_list(ListView):
    model = etapa_productiva
    template_name = 'Granja/eProductiva/granja_eProductiva_list.html'

class granja_eProductiva_delete(DeleteView):
    model = etapa_productiva
    template_name = 'Granja/eProductiva/granja_eProductiva_delete.html'
    success_url = reverse_lazy('granja:list_eProductiva')

class granja_eProductiva_edit(UpdateView):
    model = raza
    form_class = eProductiva_form
    template_name = 'Granja/eProductiva/granja_eProductiva_new.html'
    success_url = reverse_lazy('granja:list_eProductiva')
# CRUD raza
class granja_raza_new(CreateView):
    model = raza
    form_class = raza_form
    template_name = 'Granja/raza/granja_raza_new.html'
    success_url = reverse_lazy('granja:list_raza')

class granja_raza_list(ListView):
    model = raza
    template_name = 'Granja/raza/granja_raza_list.html'

class granja_raza_delete(DeleteView):
    model = raza
    template_name = 'Granja/raza/granja_raza_delete.html'
    success_url = reverse_lazy('granja:list_raza')

class granja_raza_edit(UpdateView):
    model = raza
    form_class = raza_form
    template_name = 'Granja/raza/granja_raza_new.html'
    success_url = reverse_lazy('granja:list_raza')
# CRUD proposito
class granja_proposito_new(CreateView):
    model = proposito
    form_class = proposito_form
    template_name = 'Granja/proposito/granja_proposito_new.html'
    success_url = reverse_lazy('granja:list_proposito')

class granja_proposito_list(ListView):
    model = proposito
    template_name = 'Granja/proposito/granja_proposito_list.html'

class granja_proposito_delete(DeleteView):
    model = proposito
    template_name = 'Granja/proposito/granja_proposito_delete.html'
    success_url = reverse_lazy('granja:list_proposito')

class granja_proposito_edit(UpdateView):
    model = proposito
    form_class = proposito_form
    template_name = 'Granja/proposito/granja_proposito_new.html'
    success_url = reverse_lazy('granja:list_proposito')

# CRUD Propietario
def granja_propietario_new(request):
    if request.method == 'GET':
        form = propietario_form()
        return render (request,'Granja/propietario/granja_propietario_new.html',{'form': form})
    elif request.method == 'POST':
        form = propietario_form(request.POST, request.FILES)
        if form.is_valid():
            granj = granja.objects.filter(id=request.session['idgranja'])[0]
            new_propietario = propietario(user=request.user,
                                name=form.cleaned_data["name"],
                                LastName=form.cleaned_data["LastName"],
                                IdGranja=granj,
                                correo=form.cleaned_data["correo"],
                                Telefono=form.cleaned_data["Telefono"],
                                imagePropietario=form.cleaned_data["imagePropietario"],
                                imageHierro=form.cleaned_data["imageHierro"])
            new_propietario.save()
    return HttpResponseRedirect('/granja/listar_propietario')

class granja_propietario_list(ListView):
    model = propietario
    template_name = 'Granja/propietario/granja_propietario_list.html'

class granja_propietario_delete(DeleteView):
    model = propietario
    template_name = 'Granja/propietario/granja_propietario_delete.html'
    success_url = reverse_lazy('granja:list_propietario')

class granja_propietario_edit(UpdateView):
    model = propietario
    form_class = propietario_form
    template_name = 'Granja/propietario/granja_propietario_new.html'
    success_url = reverse_lazy('granja:list_propietario')

# CRUD Insumos o servicios
def granja_serviInsu_new(request):
    if request.method == 'GET':
        form = serviInsu_form()
        return render (request,'Granja/serviInsu/granja_serviInsu_new.html',{'form': form})
    elif request.method == 'POST':
        form = serviInsu_form(request.POST, request.FILES)
        if form.is_valid():
            new_serviInsu = serviInsu(user=request.user,
                                Tipo=form.cleaned_data["Tipo"],
                                Nombre=form.cleaned_data["Nombre"],
                                Valor_Unidad=form.cleaned_data["Valor_Unidad"],
                                Detalle=form.cleaned_data["Detalle"],
                                Proveedor=form.cleaned_data["Proveedor"],
                                Telefono=form.cleaned_data["Telefono"]
                                )
            new_serviInsu.save()
    return HttpResponseRedirect('/granja/listar_serviInsu')

class granja_serviInsu_list(ListView):
    model = serviInsu
    template_name = 'Granja/serviInsu/granja_serviInsu_list.html'

class granja_serviInsu_delete(DeleteView):
    model = serviInsu
    template_name = 'Granja/serviInsu/granja_serviInsu_delete.html'
    success_url = reverse_lazy('granja:list_serviInsu')

class granja_serviInsu_edit(UpdateView):
    model = serviInsu
    form_class = serviInsu_form
    template_name = 'Granja/serviInsu/granja_serviInsu_new.html'
    success_url = reverse_lazy('granja:list_serviInsu')