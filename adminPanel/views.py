from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from pages.models import Work

class AdminProjectCreate(LoginRequiredMixin,CreateView):
    model = Work
    template_name = 'project_create.html'
    fields = '__all__'


class AdminProjectList(LoginRequiredMixin,ListView):
    model = Work
    template_name = 'home.html'


class AdminProjectUpdate(LoginRequiredMixin,UpdateView):
    model = Work
    template_name = 'project_update.html'
    fields = '__all__'


class AdminProjectDelete(LoginRequiredMixin,DeleteView):
    model = Work
    template_name = 'project_delete.html'

    success_url = reverse_lazy('home')