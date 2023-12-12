from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Basico
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    bas = Basico.objects.all()
    context = {
        'bas': bas
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def crudcreate(request):
    if request.method == 'POST':
        nomeform = request.POST['nomeform']
        telefoneform =request.POST['telefoneform']
        basico = Basico(nome=nomeform, telefone=telefoneform)
        basico.save()
        return HttpResponseRedirect('/')
    else:
            template = loader.get_template('crudcreate.html')
            return HttpResponse(template.render({}, request))
    

def crudDelete(request, id):
    basico = Basico.objects.get(id=id)
    basico.delete()
    return HttpResponseRedirect('/')

def crudupdate(request, id):
    basID = Basico.objects.get(id=id)
    bas = Basico.objects.all()
    context = {
        'bas': bas,
        'basID': basID
    }
    if request.method == 'POST':
        nomeUpdate = request.POST['nomeformupdate']
        telefoneUpdate =request.POST['telefoneformupdate']
        basicoID = Basico.objects.get(id=id)
        basicoID.nome = nomeUpdate
        basicoID.telefone = telefoneUpdate
        basicoID.save()
        return HttpResponseRedirect('/')
    else:
        template = loader.get_template('crudupdate.html')
        return HttpResponse(template.render(context, request))