from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class Login(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = "Vous êtes connecté avec succès !"
    redirect_authenticated_user = True