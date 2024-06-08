from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import AnimaisForm
from django.contrib import messages
from app.models import Animais


# Create your views here.
def home(request):
    return render(request, 'index.html')


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
