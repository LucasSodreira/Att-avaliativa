from django.shortcuts import render
from .models import Aluno

# Create your views here.
def index(request):

    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }

    return render(request, 'index.html', context)