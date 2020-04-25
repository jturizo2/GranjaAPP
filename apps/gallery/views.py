from django.shortcuts import render
from apps.gallery.forms import ImageForm
from apps.gallery.models import Image
from django.http import HttpResponseRedirect

def upload_image(request):
    if request.method == 'GET':
        return render(request, 'gallery/upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(  image = form.cleaned_data["image"],
                                name = form.cleaned_data["name"]
                                )
            new_image.save()
            return HttpResponseRedirect('/gallery/image_gallery/')

def image_gallery(request,category_id):
    images = Image.objects.get(name=category_id)
    return render(request, 'gallery/image_gallery.html', {'images': images})