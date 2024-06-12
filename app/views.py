from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import AnimaisForm
from django.contrib import messages
from app.models import Animais
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    data = {}
    all = Animais.objects.all()
    paginator = Paginator(all, 6)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def adminAccg(request):
    data = {}
    data['db'] = Animais.objects.all()
    return render(request, 'admin.html', data)


def cadastro(request):
    data = {}
    data['form'] = AnimaisForm()
    return render(request, 'cadastro.html', data)


def create(request):
    form = AnimaisForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Animal cadastrado com sucesso!')
        return redirect('adminAccg')


def animal(request, pk):
    data = {}
    data['db'] = Animais.objects.get(pk=pk)
    return render(request, 'animal.html', data)


def editar(request, pk):
    data = {}
    data['db'] = Animais.objects.get(pk=pk)
    data['form'] = AnimaisForm(instance=data['db'])
    return render(request, 'cadastro.html', data)


def atualizar(request, pk):
    data = {}
    data['db'] = Animais.objects.get(pk=pk)
    form = AnimaisForm(request.POST, instance=data['db'])
    if form.is_valid():
        form.save()
        messages.success(request, 'Animal atualizado com sucesso!')
        return redirect('adminAccg')

def deletar(request, pk):
    db = Animais.objects.get(pk=pk)
    db.delete()
    return redirect('adminAccg')

def help(request):
    return render(request, 'help.html')

def contato(request):
    return render(request, 'contato.html')

def filtro(request):
    data = {}
    tipo = request.GET.get('tipo')
    sexo = request.GET.get('sexo')
    porte = request.GET.get('porte')

    data['db'] = Animais.objects.all()

    if tipo:
        data['db'] = data['db'].filter(tipo__icontains=tipo)
    if sexo:
        data['db'] = data['db'].filter(sexo__icontains=sexo)
    if porte:
        data['db'] = data['db'].filter(porte__icontains=porte)

    return render(request, 'filtro.html', data)

def paginaAnimal(request, pk):
    data = {}
    data['animal'] = Animais.objects.get(pk=pk)
    return render(request, 'paginaAnimal.html', data)

def loginAdmin(request):
    return render(request,'login.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/admin-accg/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'login.html',data)