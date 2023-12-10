from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Site
from .forms import SiteForm


class Login(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = "Vous êtes connecté avec succès !"
    redirect_authenticated_user = True


class Logout(LogoutView):
    next_page = reverse_lazy('login')


def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Votre compte a été créé avec succès et vous êtes maintenant connecté.')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Erreur dans le champ {field}: {error}')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def Dashboard(request):
    site_form = SiteForm(request.POST or None)
    if request.method == 'POST' and site_form.is_valid():
        new_site = site_form.save(commit=False)
        new_site.user = request.user
        new_site.save()
        return redirect('dashboard')

    sites = Site.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'site_form': site_form, 'sites': sites})


@login_required
def edit_site(request, site_id):
    site = get_object_or_404(Site, id=site_id, user=request.user)
    site_form = SiteForm(request.POST or None, instance=site)
    if request.method == 'POST' and site_form.is_valid():
        site_form.save()
        return redirect('dashboard')

    return render(request, 'dashboard.html', {'site_form': site_form, 'edit_site': site})


@login_required
def delete_site(request, site_id):
    site = get_object_or_404(Site, id=site_id, user=request.user)
    site.delete()
    return redirect('dashboard')
