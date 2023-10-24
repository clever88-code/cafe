from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from .forms import *
from datetime import date


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

class Register(CreateView):
    form_class = RegisterUserForms
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"

    def form_valid(self, form):
        user = form.save()
        g, created = Group.objects.get_or_create(name='clients')
        g.user_set.add(user)
        return super().form_valid(form)
    

class LoginUser(LoginView):
    form_class = LoginUserForms
    template_name = 'registration/login.html'