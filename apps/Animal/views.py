from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Animal.forms import animalForm
from apps.Animal.models import animal
# Create your views here.
def index(request):
    return render(request, 'Animal/index.html')

def animal_form(request):
    if request.method = 'POST':
        form = animalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('animal/index.html')
    else:
        form = animalForm()
    return render(request,'animal/Animal_form.html',{'form': form})

def animal_list(request):
    amimales = animal.objects.all().order_by('id')
    contexto = {'animal': animales}
    return render(request, 'animal/animal_list.html', contexto)

def animal_edit(request, id_animal):
    animal = animal.objects.get(id=id_animal)
    if request.method = 'GET':
        form = animalForm(instance=animal)
    else:
        form = animalForm(request.POST,instance=animal)
        if form.is_valid():
            form.save()
        return redirect('animal/animal_list.html')
    return  render(request,'Animal/animal_form.html',{'form': form})

def animal_delete(request, id_animal):
    animal = animal.Objects.get(id=id_animal)
    if request.method = 'POST':
        animal.delete()
        return redirect('Animal/animal_list.html')
    return  render(request,'Animal/animal_delete.html',{'animal': animal})




