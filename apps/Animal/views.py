from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Animal.forms import animalForm
from apps.Animal.models import animal
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'Animal/index.html')

def animal_form(request):
    if request.method == 'POST':
        form = animalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('animal:list')
    else:
        form = animalForm()
    return render(request,'animal/Animal_form.html',{'form': form})

@login_required
def animal_list(request):
    animales = animal.objects.all().order_by('id')
    contexto = {'animals': animales}
    return render(request, 'animal/animal_list.html', contexto)

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

def animal_delete(request, id_animal):
    animals = animal.objects.get(id=id_animal)
    if request.method == 'POST':
        animals.delete()
        return redirect('animal:list')
    return  render(request,'Animal/animal_delete.html',{'animal': animals})




