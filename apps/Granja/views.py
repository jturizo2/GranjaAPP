from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,UpdateView, DeleteView
from apps.Granja.models import granja
from apps.Granja.forms import granja_from
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'Granja/index.html')

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
    

