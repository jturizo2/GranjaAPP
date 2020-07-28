from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Animal.forms import animalForm,animalFilter
from apps.Animal.models import animal, concepto
from apps.Granja.models import granja
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from apps.trans.models import transaction,TypeTrans,ClassTrans
import datetime
import csv
import json

from django.http import JsonResponse

animalesDescargar = []

@login_required
def index(request):
    return render(request, 'Animal/index.html')

@login_required
def animal_form(request):
    if request.method == 'POST':
        form = animalForm(request.POST, request.FILES)
        if form.is_valid():
            granj = granja.objects.filter(id=request.session['idgranja'])[0]
            new_animal = animal(IdGranja=granj,
                                estado="Activo",
                                image=form.cleaned_data["image"],
                                Codigo_animal=form.cleaned_data["Codigo_animal"],
                                concepto=form.cleaned_data["concepto"],
                                nombre=form.cleaned_data["nombre"],
                                Valor_inicial=form.cleaned_data["Valor_inicial"],
                                Genero=form.cleaned_data["Genero"],
                                Etapa_productiva=form.cleaned_data["Etapa_productiva"],
                                Raza=form.cleaned_data["Raza"],
                                propietario=form.cleaned_data["propietario"],
                                Proposito=form.cleaned_data["Proposito"],
                                Fecha_recibida=form.cleaned_data["Fecha_recibida"],
                                Fecha_nacimiento=form.cleaned_data["Fecha_nacimiento"],
                                Código_mama=form.cleaned_data["Código_mama"],
                                Código_papa=form.cleaned_data["Código_papa"])
            new_animal.save()
            return redirect('animal:list')
    else:
        form = animalForm()
    contexto = {'form': form,
                'granja': request.session['granja']}
    return render(request,'Animal/animal_form.html',contexto)

@login_required
def animal_list(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    animales = animal.objects.filter(IdGranja=granj).order_by('id').exclude(estado="Inactivo")
    filters = animalFilter()
    contexto = {'animals': animales,
                'granja': request.session['granja'],
                'filters':filters}
    return render(request, 'Animal/animal_list.html', contexto)

@login_required
def animal_view(request, id_animal):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    animales = animal.objects.filter(IdGranja=granj,id=id_animal).order_by('id')
    contexto = {'animals': animales,
                'granja': request.session['granja']}
    return render(request, 'Animal/animal_card.html', contexto)


@login_required
def animal_descargar(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response, delimiter=';')
    
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    return response

@login_required
def animal_search(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    a = Q(IdGranja=granj)

    if request.method == 'POST':
        filters = animalFilter(request.POST)
        if True:
            b = request.POST["Codigo_animal"]
            if b != None:
                a = a & Q(Codigo_animal__contains=b)

            b = request.POST["nombre"]
            if b != '':
                a = a & Q(nombre__contains=b)
            
            b = request.POST["Código_mama"]
            if b != '':
                a = a & Q(Código_mama__contains=b)

            b = request.POST["Código_papa"]
            if b != '':
                a = a & Q(Código_papa__contains=b)

            b = request.POST["concepto"]
            if b != '':
                a = a & Q(concepto=b)

            b = request.POST["Genero"]
            if b != '':
                a = a & Q(Genero=b)
            
            b = request.POST["Etapa_productiva"]
            if b != '':
                a = a & Q(Etapa_productiva=b)

            b = request.POST["Raza"]
            if b != '':
                a = a & Q(Raza=b)

            b = request.POST["propietario"]
            if b != '':
                a = a & Q(propietario=b)
            
            b = request.POST["Proposito"]
            if b != '':
                a = a & Q(Proposito=b)
            
            b = Q(Fecha_recibida__gte=request.POST["Fecha_recibidai"]) & Q(Fecha_recibida__lte=request.POST["Fecha_recibidaf"]) | Q(Fecha_recibida=None)
            a = a & b
            
            b = Q(Fecha_nacimiento__gte=request.POST["Fecha_nacimientoi"]) & Q(Fecha_nacimiento__lte=request.POST["Fecha_nacimientof"]) | Q(Fecha_nacimiento=None)
            a = a & b
    #------------------------------------------------------------
    animales = animal.objects.filter(a).order_by('id')
    contexto = {'animals': animales,
                'granja': request.session['granja'],
                'filters':filters,}

    if "descargar" in request.POST:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Resultados_animales.csv"'
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response, delimiter=';')

        writer.writerow(["#",
                           "Código de animal",
                           "Estado",
                            "Nombre",
                            "Granja",
                            "Concepto",
                            "Valor_inicial",
                            "Genero",
                            "Etapa_productiva",
                            "Raza",
                            "propietario",
                            "Proposito",
                            "Fecha_recibida",
                            "Fecha_nacimiento",
                            "Código_papa",
                            "Código_mama",
                            "Edad",
                            "Tiempo Custodia"])

        x = 1
        for ani in animales:
            hoy = datetime.date.today()
            edad = "No aplica"
            if  ani.Fecha_nacimiento != None:
                edad = str(hoy.year - ani.Fecha_nacimiento.year) + " A " +str(hoy.month - ani.Fecha_nacimiento.month) + " M "
            
            tiempo = "No aplica"
            if ani.Fecha_recibida != None:
                tiempo = str(hoy.year - ani.Fecha_recibida.year) + " A " +str(hoy.month - ani.Fecha_recibida.month) + " M "
            

            writer.writerow([str(x),
                            '"' + ani.Codigo_animal + '"',
                            ani.estado,
                            ani.nombre,
                            ani.IdGranja,
                            ani.concepto,
                            ani.Valor_inicial,
                            ani.Genero,
                            ani.Etapa_productiva,
                            ani.Raza,
                            ani.propietario,
                            ani.Proposito,
                            ani.Fecha_recibida,
                            ani.Fecha_nacimiento,
                            ani.Código_papa,
                            ani.Código_mama,
                            edad,
                            tiempo])
            x = x + 1
        return response

    return render(request, 'Animal/animal_list.html', contexto)

@login_required
def animal_edit(request, id_animal):
    animals = animal.objects.get(id=id_animal)
    if request.method == 'GET':
        form = animalForm(instance=animals)
    else:
        form = animalForm(request.POST,request.FILES,instance=animals)
        if form.is_valid():
            form.save()
        return redirect('animal:list')
    return  render(request,'Animal/animal_form.html',{'form': form})

@login_required
def animal_delete(request, id_animal):
    animals = animal.objects.get(id=id_animal)
    if request.method == 'POST':
        animals.delete()
        return redirect('animal:list')
    return  render(request,'Animal/animal_delete.html',{'animal': animals})




