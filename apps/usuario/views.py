from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import registroFormUser

class registar_usuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = registroFormUser
    success_url = reverse_lazy("login")

