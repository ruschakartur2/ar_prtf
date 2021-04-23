from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.db.models import Q

from pages.models import Work


class ProjectList(ListView):
    template_name = 'home.html'
    model = Work


class ProjectDetail(DetailView):
    template_name = 'project_detail.html'
    model = Work

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['lasted'] = Work.objects.filter(~Q(id=self.object.id))
        return context