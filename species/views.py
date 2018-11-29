from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Species

@csrf_exempt
def tree(request):
    if request.method != 'POST':
        species = Species.objects.get(id=1)
        species.init_tree_structure(2)
        template = loader.get_template('species/tree.html')
        context = {
            'species': species,
        }
        return HttpResponse(template.render(context, request))
    else:
        species = Species.objects.get(id=request.POST.get('id'))
        if(request.POST.get('childs') == '0'):
            species.init_tree_structure(1)
        else:
            species.init_tree_structure(0)
        template = loader.get_template('species/species_with_childs.html')
        context = {
            'species': species,
        }
        return HttpResponse(template.render(context, request))

def autocomplete(request):
    if request.is_ajax():
        species = Species.objects.filter(title__startswith=request.GET.get('term', '').capitalize())
        results = [spec.title for spec in species]
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@csrf_exempt
def search(request):
    if(request.method == 'POST'):
        species = Species.objects.get(title=request.POST.get('name'))
        species = species.get_root()
        template = loader.get_template('species/species_with_childs.html')
        context = {
            'species': species,
        }
        return HttpResponse(template.render(context, request))
