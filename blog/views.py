from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post, Info, Contacto

def index(request):
    return render(request, 'blog/index.html')


class InfoList(ListView):
    model = Info
    template_name = 'blog/base.html'
    #template_name = 'blog/index.html'
    #template_name = 'blog/nosotros.html'

class InfoAbout(ListView):
    model = Info
    template_name = 'blog/nosotros.html'

class ContactoCreate(CreateView):
    model = Contacto
    fields = ['nombres', 'apellidos', 'correo', 'asunto', 'mensaje']
    #template_name = 'blog/contacto_form.html'