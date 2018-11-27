from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Species

def tree(request):
    if request.method != 'POST':
        species = Species.objects.get(id=200)
        species = species.get_root()
        #species.init_tree_structure(2)
        template = loader.get_template('tree.html')
        context = {
            'species': species,
        }
        return HttpResponse(template.render(context, request))
    else:
        species = Species.objects.get(id=180)
        species = species.get_root()
        return render(request, 'tree.html', {'species': species})

def autocompleteSpecies(request):
    species = Species.objects.filter(title__contains=request.REQUEST['search'])
    results = [spec for spec in species]
