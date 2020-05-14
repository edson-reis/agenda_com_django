from django.shortcuts import render, redirect
from core.models import ListaEvento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
#def index(request):
#    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect ('/')
        else:
            messages.error(request,"Usuário e/ou senha inválidos.")
        return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    #eventos = ListaEvento.objects.all()
    eventos = ListaEvento.objects.filter(usuario=usuario)
    dados = {'eventos':eventos}
    return render(request,'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = ListaEvento.objects.get(id=id_evento)
    return render (request,'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            ListaEvento.objects.filter(id=id_evento).update(titulo=titulo,
                                                            descricao=descricao,
                                                            data_evento=data_evento)
        else:
            ListaEvento.objects.create(titulo=titulo,
                                       descricao=descricao,
                                       data_evento=data_evento,
                                       usuario=usuario)
            return redirect('/')
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = ListaEvento.objects.get(id=id_evento)
    if (usuario==evento.usuario):
        evento.delete()
    return redirect('/')
