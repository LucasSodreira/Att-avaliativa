from django.shortcuts import render, redirect
from .models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
    }
    return render(request, 'index.html', context)


def editar_item(request, item_id):
    # Lógica para editar um item
    return redirect('lista_itens')

def remover_item(request, item_id):
    # Lógica para remover um item
    return redirect('lista_itens')
