from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tarefa

# Create your views here.
def home(request):
    return render(request, "home.html")

def tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "tarefas.html", {"tarefas": tarefas})

def detalhe(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, "detalhe.html", {"tarefa": tarefa})
