from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from apps.Granja.models import granja
from apps.Animal.models import animal
from apps.trans.forms import mov_form, movFilter, InsServFilter, InsServ_form,InsServ_form_edit
from apps.trans.models import transaction,TypeTrans, transactionserviInsu,TypeTransserviInsu,serviInsu
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo Trans")

# COmpra y venta de animales 
@login_required
def mov_new(request):
    if request.method == 'POST':
        form = mov_form(request.POST)
        if form.is_valid():
            
            granj = granja.objects.filter(id=request.session['idgranja'])[0]
            tra = TypeTrans.objects.filter(Tipo='Comercio')[0]
            us = User.objects.get(username=request.user)
            new_transaction = transaction(
                                user=us,
                                IdGranja=granj,
                                TypeTrans= tra,
                                classTrans=form.cleaned_data["classTrans"],
                                date=form.cleaned_data["date"],
                                AnimalCode=form.cleaned_data["AnimalCode"],
                                detail=form.cleaned_data["detail"],
                                Value=form.cleaned_data["Value"],
                                quantity=0
                                )
            new_transaction.save()
        return redirect('trans:list')
    else:
        form = mov_form()
    contexto = {'form': form,
                'granja': request.session['granja']}

    return render(request,'Animal/comercio/mov_new.html',contexto)

@login_required
def mov_list(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    movs = transaction.objects.filter(Q(IdGranja=granj) & Q(user=request.user) ).order_by('id')
    filters = movFilter()
    contexto = {'movs': movs,
                'granja': request.session['granja'],
                'filters':filters}
    return render(request,'Animal/comercio/comercio_list.html', contexto)

@login_required

def search_mov(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    a = Q(IdGranja=granj) & Q(user=request.user)
    filters = movFilter()

    if request.method == 'POST':
        filters = movFilter(request.POST)
        if True:

            b = animal.objects.filter(IdGranja=granj, Codigo_animal__contains=request.POST["AnimalCode"])
    
            if len(request.POST["AnimalCode"]) != 0:
                a = a & Q(AnimalCode=b[0])

            b = request.POST["classTrans"]


            if len(b) != 0:
                a = a & Q(classTrans=b)

            b = Q(date__gte=request.POST["datei"]) & Q(date__lte=request.POST["datef"])
            a = a & b

        pass
    #------------------------------------------------------------
    movs = transaction.objects.filter(a).order_by('id')
    contexto = {'movs': movs,
                'granja': request.session['granja'],
                'filters':filters}

    return render(request, 'Animal/comercio/comercio_list.html', contexto)


@login_required
def mov_edit(request, id_mov):
    tr = transaction.objects.get(id=id_mov)
    if request.method == 'GET':
        form = mov_form(instance=tr)
    else:
        form = mov_form(request.POST,instance=tr)
        if form.is_valid():
            form.save()
        return redirect('trans:list')
    return  render(request,'Animal/comercio/mov_new.html',{'form': form})

@login_required
def mov_delete(request, id_mov):
    tr = transaction.objects.get(id=id_mov)
    if request.method == 'POST':
        tr.delete()
        return redirect('trans:list')
    return  render(request,'Animal/comercio/mov_delete.html',{'data': tr})

# CRUD Insumos Servicios
# ok
@login_required
def InsServ_new(request):
    if request.method == 'POST':
        form = InsServ_form(request.POST)
        if form.is_valid():
            granj = granja.objects.filter(id=request.session['idgranja'])[0]
            us = User.objects.get(username=request.user)    

            tra = TypeTransserviInsu.objects.filter(Tipo=form.cleaned_data["Tipo"])[0]
            comp = serviInsu.objects.filter(Nombre=form.cleaned_data["concepto"])[0]

            new_transaction = transactionserviInsu(
                                IdGranja=granj,
                                user=us,
                                Tipo= tra,
                                concepto=comp,
                                date=form.cleaned_data["date"],
                                detail=form.cleaned_data["detail"],
                                Value=comp.Valor_Unidad,
                                quantity=form.cleaned_data["quantity"],
                                Total= float(form.cleaned_data["quantity"]) * float(comp.Valor_Unidad)
                                )

            new_transaction.save()
        return redirect('trans:list_InsServ')
    else:
        form = InsServ_form()
    contexto = {'form': form,
                'granja': request.session['granja']}

    return render(request,'Animal/InsuServi/mov_new.html',contexto)

@login_required
#OK
def InsServ_list(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    movs = transactionserviInsu.objects.filter(Q(IdGranja=granj) & Q(user=request.user) ).order_by('id')
    filters = InsServFilter()
    contexto = {'movs': movs,
                'granja': request.session['granja'],
                'filters':filters}
    return render(request,'Animal/InsuServi/mov_list.html', contexto)

@login_required

def search_InsServ(request):
    granj = granja.objects.filter(id=request.session['idgranja'])[0]
    us = User.objects.get(username=request.user) 

    a = Q(IdGranja=granj) & Q(user=request.user)
    filters = InsServFilter()

    if request.method == 'POST':
        filters = InsServFilter(request.POST)
        if True:
            print(request.POST["Tipo"])
            if len(request.POST["Tipo"]) != 0:
                b = TypeTransserviInsu.objects.filter(id=request.POST["Tipo"],user=us)
                a = a & Q(Tipo=b[0])

            b = Q(date__gte=request.POST["datei"]) & Q(date__lte=request.POST["datef"])
            a = a & b

        pass
    #------------------------------------------------------------
    movs = transactionserviInsu.objects.filter(a).order_by('id')
    contexto = {'movs': movs,
                'granja': request.session['granja'],
                'filters':filters}

    return render(request, 'Animal/InsuServi/mov_list.html', contexto)


@login_required
def InsServ_edit(request, id_mov):
    tr = transactionserviInsu.objects.get(id=id_mov)
    if request.method == 'GET':
        form = InsServ_form_edit(instance=tr)
    else:
        form = InsServ_form_edit(request.POST,instance=tr)
        if form.is_valid():
            #Actualizar los demas campos
            form.save()
            #Actualiza campo total
            us = User.objects.get(username=request.user)    
            total= float(form.cleaned_data["quantity"]) * float(form.cleaned_data["Value"])   

            transactionserviInsu.objects.filter(id=id_mov).update(Total=total)

        return redirect('trans:list_InsServ')
    return  render(request,'Animal/InsuServi/mov_new.html',{'form': form})

@login_required
def InsServ_delete(request, id_mov):
    tr = transactionserviInsu.objects.get(id=id_mov)
    if request.method == 'POST':
        tr.delete()
        return redirect('trans:list_InsServ')
    return  render(request,'Animal/InsuServi/mov_delete.html',{'data': tr})


