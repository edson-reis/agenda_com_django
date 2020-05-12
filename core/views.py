from django.shortcuts import render, redirect
from core.models import ListaEvento

# Create your views here.
#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    eventos = ListaEvento.objects.all()
    #eventos = ListaEvento.objects.filter(usuario=usuario)
    dados = {'eventos':eventos}
    return render(request,'agenda.html', dados)
