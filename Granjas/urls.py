from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^granja/', include('apps.Granja.urls', namespace='granja')),
    url(r'^granjero/', include('apps.Granjero.urls')),
    url(r'^transaccion/', include('apps.trans.urls', namespace='trans')),
    url(r'^animal/', include('apps.Animal.urls', namespace='animal')),

    #Gestion de usuarios
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),

    #Logouut and Login
    url(r'^accounts/login/', LoginView.as_view(template_name='usuario/index.html'), name='login'),
    url(r'^$', LoginView.as_view(template_name='usuario/index.html'), name='login1'),
    url(r'^logout/', logout_then_login, name='logout'),

    #Restablecer contraseña
    url(r'^reset/password_reset', PasswordResetView.as_view(template_name='registro/password_reset_form.html', email_template_name='registro/password_reset_email.html', success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    url(r'^/reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done', PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'),name='password_reset_complete'),

    #Imagenes
    path('gallery/', include('apps.gallery.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)