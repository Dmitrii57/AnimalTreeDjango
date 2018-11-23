from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template import loader

from .models import List

def tree(request):
    species = List.objects.get(id=1)
    species.init_tree_structure(2)
    template = loader.get_template('tree.html')
    context = {
        'species': species,
    }
    return HttpResponse(template.render(context, request))

class TreeList(ListView):
    model = List

class TreeDetail(DetailView):
    model = List