from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
    }
    return render(request, 'index.html', context)


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})


def editar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})


def excluir_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    aluno.delete()
    return redirect('index')