from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Animal.forms import animalForm
from apps.Animal.models import animal
from apps.Granja.models import granja
from django.contrib.auth.decorators import login_required

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
                                image=form.cleaned_data["image"],
                                Codigo_animal=form.cleaned_data["Codigo_animal"],
                                concepto=form.cleaned_data["concepto"],
                                nombre=form.cleaned_data["nombre"],
                                Valor_inicial=form.cleaned_data["Valor_inicial"],
                                Genero=form.cleaned_data["Genero"],
                                Etapa_productiva=form.cleaned_data["Etapa_productiva"],
                                Raza=form.cleaned_data["Raza"],
                                Hierro=form.cleaned_data["Hierro"],
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
    return render(request,'animal/Animal_form.html',contexto)

@login_required
def animal_list(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    animales = animal.objects.filter(IdGranja=granj).order_by('id')
    contexto = {'animals': animales,
                'granja': request.session['granja']}
    return render(request, 'animal/animal_list.html', contexto)
@login_required
def animal_edit(request, id_animal):
    animals = animal.objects.get(id=id_animal)
    if request.method == 'GET':
        form = animalForm(instance=animals)
    else:
        form = animalForm(request.POST,instance=animals)
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




