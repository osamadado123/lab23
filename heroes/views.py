from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import heroes


class heroesListView(ListView):
    template_name = "heroes/heroes-list.html"
    model = heroes


class heroesDetailView(DetailView):
    template_name = "heroes/heroes-detail.html"
    model = heroes


class heroesCreateView(CreateView):
    template_name = "heroes/heroes-create.html"
    model = heroes
    fields = [
  
    
    "name",
    "img_url",
    "attack_type",
    "roles",
    "creator"
    
  
]


class heroesUpdateView(UpdateView):
    template_name = "heroes/heroes-update.html"
    model = heroes
    fields = [
  
    
    "name",
    "img_url",
    "attack_type",
    "roles",
    "creator"
    
  
]


class heroesDeleteView(DeleteView):
    template_name = "heroes/heroes-delete.html"
    model = heroes
    success_url = reverse_lazy("heroes-list")