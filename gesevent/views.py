from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from gesevent.form import TematicaForm


# Create your views here.
def tematica_crear(request):
    if request.method == 'POST':
        form = TematicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tematica_crear')
    else:
        form = TematicaForm()
    return render_to_response('gesevent/tematica_crear.html', {'form': form},
                              context_instance=RequestContext(request))
